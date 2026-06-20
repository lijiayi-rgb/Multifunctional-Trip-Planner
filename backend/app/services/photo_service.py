"""图片服务（基于高德地图 POI 搜索）"""

import requests
from typing import List, Optional
from ..config import get_settings
import os

class PhotoService:
    """图片服务类（使用高德地图 POI 搜索获取景点图片）"""
    
    def __init__(self):
        """初始化服务"""
        settings = get_settings()
        self.amap_web_key = settings.amap_api_key  # 安全！从配置读取
        self.amap_poi_url = "https://restapi.amap.com/v3/place/text"
    
    def search_photos(self, query: str, city: str = "北京", per_page: int = 5) -> List[dict]:
        """通过高德 POI 搜索获取图片"""
        try:
            params = {
                "keywords": query,
                "city": city,
                "key": self.amap_web_key,
                "extensions": "all",
                "offset": per_page
            }
            
            response = requests.get(self.amap_poi_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if data.get("status") != "1":
                print(f"⚠️ 高德 POI 搜索失败: {data.get('info')}")
                return []
            
            pois = data.get("pois", [])
            photos = []
            for poi in pois:
                if "photos" in poi and len(poi["photos"]) > 0:
                    for photo in poi["photos"]:
                        photo_url = photo.get("url", "")
                        if photo_url.startswith("//"):
                            photo_url = "https:" + photo_url
                        elif not photo_url.startswith("http"):
                            photo_url = "https://" + photo_url
                        
                        photos.append({
                            "id": photo.get("id", ""),
                            "url": photo_url,
                            "thumb": photo_url,
                            "description": poi.get("name", query),
                            "photographer": "高德地图"
                        })
            
            return photos[:per_page]
            
        except Exception as e:
            print(f"❌ 高德图片搜索失败: {str(e)}")
            return []
    
    def get_photo_url(self, query: str, city: str = "北京") -> Optional[str]:
        """获取单张图片URL"""
        photos = self.search_photos(query, city=city, per_page=1)
        if photos:
            return photos[0].get("url")
        return None


# 全局服务实例
_photo_service = None


def get_photo_service() -> PhotoService:
    """获取图片服务实例(单例模式)"""
    global _photo_service
    
    if _photo_service is None:
        _photo_service = PhotoService()
    
    return _photo_service