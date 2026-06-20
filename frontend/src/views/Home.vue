<template>
  <div class="home-container">
    <!-- 动态地球背景 -->
    <div class="earth-bg">
      <div class="earth-sphere"></div>
      <div class="dark-overlay"></div>
    </div>

    <!-- 页面标题 -->
    <div class="page-header">
      <div class="icon-wrapper">
        <span class="icon"></span>
      </div>
      <h1 class="page-title">我是你的旅行规划助手哒哒！！！❤</h1>
      <p class="page-subtitle">期待与你一起探索世界的美好！</p>
    </div>

    <!-- 表单卡片 (花边半透明) -->
    <a-card class="form-card" :bordered="false">
      <a-form
        :model="formData"
        layout="vertical"
        @finish="handleSubmit"
      >
        <!-- 第一步: 旅行期许 (提前，强调个人期待) -->
        <div class="form-section lace-border">
          <div class="section-header">
            <span class="section-icon">💬</span>
            <span class="section-title">旅行期许</span>
          </div>

          <a-form-item name="free_text_input">
            <a-textarea
              v-model:value="formData.free_text_input"
              placeholder="写下你的旅行期许，例如: 想去看升旗、需要无障碍设施、对海鲜过敏..."
              :rows="4"
              size="large"
              class="custom-textarea lace-input"
            />
          </a-form-item>
        </div>

        <!-- 第二步: 目的地和日期 -->
        <div class="form-section lace-border">
          <div class="section-header">
            <span class="section-icon">📍</span>
            <span class="section-title">目的地与日期</span>
          </div>

          <a-row :gutter="24">
            <a-col :span="8">
              <a-form-item name="city" :rules="[{ required: true, message: '请输入目的地城市' }]">
                <template #label>
                  <span class="form-label">目的地城市</span>
                </template>
                <a-input
                  v-model:value="formData.city"
                  placeholder="例如: 北京"
                  size="large"
                  class="custom-input lace-input"
                >
                  <template #prefix>
                    <span style="color: #00d4ff;">🏙️</span>
                  </template>
                </a-input>
              </a-form-item>
            </a-col>
            <a-col :span="6">
              <a-form-item name="start_date" :rules="[{ required: true, message: '请选择开始日期' }]">
                <template #label>
                  <span class="form-label">开始日期</span>
                </template>
                <a-date-picker
                  v-model:value="formData.start_date"
                  style="width: 100%"
                  size="large"
                  class="custom-input lace-input"
                  placeholder="选择日期"
                />
              </a-form-item>
            </a-col>
            <a-col :span="6">
              <a-form-item name="end_date" :rules="[{ required: true, message: '请选择结束日期' }]">
                <template #label>
                  <span class="form-label">结束日期</span>
                </template>
                <a-date-picker
                  v-model:value="formData.end_date"
                  style="width: 100%"
                  size="large"
                  class="custom-input lace-input"
                  placeholder="选择日期"
                />
              </a-form-item>
            </a-col>
            <a-col :span="4">
              <a-form-item>
                <template #label>
                  <span class="form-label">旅行天数</span>
                </template>
                <div class="days-display-compact lace-input">
                  <span class="days-value">{{ formData.travel_days }}</span>
                  <span class="days-unit">天</span>
                </div>
              </a-form-item>
            </a-col>
          </a-row>
        </div>

        <!-- 第三步: 偏好设置 -->
        <div class="form-section lace-border">
          <div class="section-header">
            <span class="section-icon">⚙️</span>
            <span class="section-title">偏好设置</span>
          </div>

          <a-row :gutter="24">
            <a-col :span="8">
              <a-form-item name="transportation">
                <template #label>
                  <span class="form-label">交通方式</span>
                </template>
                <a-select v-model:value="formData.transportation" size="large" class="custom-select lace-input">
                  <a-select-option value="公共交通">🚇 公共交通</a-select-option>
                  <a-select-option value="自驾">🚗 自驾</a-select-option>
                  <a-select-option value="步行">🚶 步行</a-select-option>
                  <a-select-option value="混合">🔀 混合</a-select-option>
                </a-select>
              </a-form-item>
            </a-col>
            <a-col :span="8">
              <a-form-item name="accommodation">
                <template #label>
                  <span class="form-label">住宿偏好</span>
                </template>
                <a-select v-model:value="formData.accommodation" size="large" class="custom-select lace-input">
                  <a-select-option value="经济型酒店">💰 经济型酒店</a-select-option>
                  <a-select-option value="舒适型酒店">🏨 舒适型酒店</a-select-option>
                  <a-select-option value="豪华酒店">⭐ 豪华酒店</a-select-option>
                  <a-select-option value="民宿">🏡 民宿</a-select-option>
                </a-select>
              </a-form-item>
            </a-col>
            <a-col :span="8">
              <a-form-item name="preferences">
                <template #label>
                  <span class="form-label">旅行偏好</span>
                </template>
                <div class="preference-tags">
                  <a-checkbox-group v-model:value="formData.preferences" class="custom-checkbox-group">
                    <a-checkbox value="历史文化" class="preference-tag">🏛️ 历史文化</a-checkbox>
                    <a-checkbox value="自然风光" class="preference-tag">🏞️ 自然风光</a-checkbox>
                    <a-checkbox value="美食" class="preference-tag">🍜 美食</a-checkbox>
                    <a-checkbox value="游乐项目" class="preference-tag">🎢 游乐项目</a-checkbox>
                    <a-checkbox value="购物" class="preference-tag">🛍️ 购物</a-checkbox>
                    <a-checkbox value="艺术" class="preference-tag">🎨 艺术</a-checkbox>
                    <a-checkbox value="休闲" class="preference-tag">☕ 休闲</a-checkbox>
                  </a-checkbox-group>
                </div>
              </a-form-item>
            </a-col>
          </a-row>
        </div>

        <!-- 提交按钮 -->
        <a-form-item>
          <a-button
            type="primary"
            html-type="submit"
            :loading="loading"
            size="large"
            block
            class="submit-button"
          >
            <template v-if="!loading">
              <span class="button-icon">❤</span>
              <span>开始规划我的旅行</span>
              <span class="button-icon">❤</span>
            </template>
            <template v-else>
              <span>正在生成中...</span>
            </template>
          </a-button>
        </a-form-item>

        <!-- 加载进度条 -->
        <a-form-item v-if="loading">
          <div class="loading-container lace-border">
            <a-progress
              :percent="loadingProgress"
              status="active"
              :stroke-color="{
                '0%': '#00d4ff',
                '100%': '#a855f7',
              }"
              :stroke-width="10"
            />
            <p class="loading-status">
              {{ loadingStatus }}
            </p>
          </div>
        </a-form-item>
      </a-form>
    </a-card>
  </div>
</template>

<script setup lang="ts">
// 保持原有的 script 部分完全不变
import { ref, reactive, watch } from 'vue'
import { useRouter } from 'vue-router'
import { message } from 'ant-design-vue'
import { generateTripPlan } from '@/services/api'
import type { TripFormData } from '@/types'
import type { Dayjs } from 'dayjs'

const router = useRouter()
const loading = ref(false)
const loadingProgress = ref(0)
const loadingStatus = ref('')

const formData = reactive<TripFormData & { start_date: Dayjs | null; end_date: Dayjs | null }>({
  city: '',
  start_date: null,
  end_date: null,
  travel_days: 1,
  transportation: '公共交通',
  accommodation: '经济型酒店',
  preferences: [],
  free_text_input: ''
})

watch([() => formData.start_date, () => formData.end_date], ([start, end]) => {
  if (start && end) {
    const days = end.diff(start, 'day') + 1
    if (days > 0 && days <= 30) {
      formData.travel_days = days
    } else if (days > 30) {
      message.warning('旅行天数不能超过30天')
      formData.end_date = null
    } else {
      message.warning('结束日期不能早于开始日期')
      formData.end_date = null
    }
  }
})

const handleSubmit = async () => {
  if (!formData.start_date || !formData.end_date) {
    message.error('请选择日期')
    return
  }

  loading.value = true
  loadingProgress.value = 0
  loadingStatus.value = '正在初始化...'

  const progressInterval = setInterval(() => {
    if (loadingProgress.value < 90) {
      loadingProgress.value += 10

      if (loadingProgress.value <= 30) {
        loadingStatus.value = '🔍 正在搜索景点...'
      } else if (loadingProgress.value <= 50) {
        loadingStatus.value = '🌤️ 正在查询天气...'
      } else if (loadingProgress.value <= 70) {
        loadingStatus.value = '🏨 正在推荐酒店...'
      } else {
        loadingStatus.value = '📋 正在生成行程计划...'
      }
    }
  }, 500)

  try {
    const requestData: TripFormData = {
      city: formData.city,
      start_date: formData.start_date.format('YYYY-MM-DD'),
      end_date: formData.end_date.format('YYYY-MM-DD'),
      travel_days: formData.travel_days,
      transportation: formData.transportation,
      accommodation: formData.accommodation,
      preferences: formData.preferences,
      free_text_input: formData.free_text_input
    }

    const response = await generateTripPlan(requestData)

    clearInterval(progressInterval)
    loadingProgress.value = 100
    loadingStatus.value = '✅ 完成!'

    if (response.success && response.data) {
      sessionStorage.setItem('tripPlan', JSON.stringify(response.data))
      message.success('旅行计划生成成功!')
      setTimeout(() => {
        router.push('/result')
      }, 500)
    } else {
      message.error(response.message || '生成失败')
    }
  } catch (error: any) {
    clearInterval(progressInterval)
    message.error(error.message || '生成旅行计划失败，请稍后重试')
  } finally {
    setTimeout(() => {
      loading.value = false
      loadingProgress.value = 0
      loadingStatus.value = ''
    }, 1000)
  }
}
</script>

<style scoped>
/* ====== 暗黑风格：可视化地球动态背景 + 花边半透明设计 ====== */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

.home-container {
  min-height: 100vh;
  background: #0a0a0f;
  padding: 60px 20px;
  position: relative;
  overflow: hidden;
  font-family: 'Inter', sans-serif;
}

/* ---------- 动态地球背景 ---------- */
.earth-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
}

.earth-sphere {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 1200px;
  height: 1200px;
  background: url('https://cdn.mos.cms.futurecdn.net/rVj7b7wYF9MCH2G7D7uGdN-1200-80.jpg') center/cover no-repeat;
  border-radius: 50%;
  opacity: 0.25;
  filter: drop-shadow(0 0 80px rgba(0, 212, 255, 0.4));
  animation: rotateEarth 80s linear infinite;
}

@keyframes rotateEarth {
  from { transform: translate(-50%, -50%) rotate(0deg); }
  to { transform: translate(-50%, -50%) rotate(360deg); }
}

.dark-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at center, transparent 20%, rgba(10, 10, 15, 0.85) 90%);
}

/* ---------- 页面标题 (增加呼吸光晕) ---------- */
.page-header {
  text-align: center;
  margin-bottom: 50px;
  animation: fadeInDown 0.8s ease-out;
  position: relative;
  z-index: 1;
}

.icon-wrapper {
  margin-bottom: 20px;
}

.icon {
  font-size: 80px;
  display: inline-block;
  animation: bounce 2s infinite, softGlow 3s ease-in-out infinite;
  filter: drop-shadow(0 0 20px rgba(168, 85, 247, 0.7));
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

@keyframes softGlow {
  0%, 100% { filter: drop-shadow(0 0 15px rgba(168, 85, 247, 0.5)); }
  50% { filter: drop-shadow(0 0 30px rgba(0, 212, 255, 0.8)); }
}

.page-title {
  font-size: 68px;
  font-weight: 800;
  color: #ffffff;
  text-shadow: 0 0 30px rgba(0, 212, 255, 0.6), 0 0 60px rgba(168, 85, 247, 0.4);
  letter-spacing: 4px;
  margin-bottom: 16px;
}

.page-subtitle {
  font-size: 22px;
  color: #a0aec0;
  font-weight: 500;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(5px);
  display: inline-block;
  padding: 6px 28px;
  border-radius: 30px;
  border: 1px solid rgba(0, 212, 255, 0.3);
}

/* ---------- 花边半透明通用样式 ---------- */
.lace-border {
  border: 2px dashed rgba(0, 212, 255, 0.3) !important;
  box-shadow: 0 0 15px rgba(0, 212, 255, 0.1), inset 0 0 15px rgba(168, 85, 247, 0.1);
  backdrop-filter: blur(15px);
  border-radius: 24px;
}

.lace-input {
  border: 1px solid rgba(0, 212, 255, 0.25) !important;
  box-shadow: 0 0 8px rgba(0, 212, 255, 0.1), inset 0 0 8px rgba(168, 85, 247, 0.1);
  background: rgba(20, 20, 35, 0.75) !important;
  backdrop-filter: blur(12px);
  border-radius: 16px;
  transition: all 0.4s ease;
}

.lace-input:hover {
  border-color: rgba(0, 212, 255, 0.5) !important;
  box-shadow: 0 0 18px rgba(0, 212, 255, 0.25), inset 0 0 18px rgba(168, 85, 247, 0.2);
}

/* ---------- 表单卡片 ---------- */
.form-card {
  max-width: 1400px;
  margin: 0 auto;
  border-radius: 36px;
  box-shadow: 0 0 50px rgba(0, 212, 255, 0.2), 0 20px 50px rgba(0, 0, 0, 0.6);
  animation: fadeInUp 0.8s ease-out;
  position: relative;
  z-index: 1;
  background: rgba(20, 20, 30, 0.8) !important;
  backdrop-filter: blur(25px);
  border: 2px solid rgba(0, 212, 255, 0.25);
}

/* ---------- 表单分区 ---------- */
.form-section {
  margin-bottom: 32px;
  padding: 28px;
  background: rgba(30, 30, 45, 0.5);
  transition: all 0.4s ease;
}

.form-section:hover {
  background: rgba(40, 40, 60, 0.65);
  border-color: rgba(0, 212, 255, 0.6) !important;
  box-shadow: 0 0 25px rgba(0, 212, 255, 0.25), inset 0 0 25px rgba(168, 85, 247, 0.15);
  transform: scale(1.01);
}

.section-header {
  display: flex;
  align-items: center;
  margin-bottom: 24px;
  padding-bottom: 14px;
  border-bottom: 2px solid rgba(0, 212, 255, 0.5);
}

.section-icon {
  font-size: 28px;
  margin-right: 14px;
  background: linear-gradient(135deg, #00d4ff, #a855f7);
  color: white;
  width: 46px;
  height: 46px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 18px rgba(0, 212, 255, 0.5);
}

.section-title {
  font-size: 22px;
  font-weight: 700;
  color: #e2e8f0;
  text-transform: uppercase;
  letter-spacing: 2px;
}

/* ---------- 表单组件细节 ---------- */
.form-label {
  font-size: 16px;
  font-weight: 600;
  color: #cbd5e0;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* 使用花边半透明样式的输入框和选择器 */
.custom-input :deep(.ant-input),
.custom-input :deep(.ant-picker) {
  border-radius: 14px;
  color: #fff;
  font-family: 'Inter', sans-serif;
}

.custom-select :deep(.ant-select-selector) {
  border-radius: 14px !important;
  color: #fff !important;
  font-family: 'Inter', sans-serif;
}

.custom-select :deep(.ant-select-arrow) {
  color: #00d4ff;
}

.custom-textarea :deep(.ant-input) {
  border-radius: 14px;
  color: #fff;
  font-family: 'Inter', sans-serif;
}

.days-display-compact {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 44px;
  padding: 10px 18px;
  background: linear-gradient(135deg, #00d4ff, #a855f7);
  color: #fff;
  font-weight: 700;
  box-shadow: 0 0 15px rgba(0, 212, 255, 0.4);
  text-shadow: 0 1px 3px rgba(0,0,0,0.3);
}

.days-value {
  font-size: 24px;
  margin-right: 4px;
}

.days-unit {
  font-size: 14px;
  opacity: 0.95;
}

/* 偏好标签花边效果 */
.custom-checkbox-group {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  width: 100%;
}

.preference-tag :deep(.ant-checkbox-wrapper) {
  margin: 0 !important;
  padding: 8px 20px;
  border: 1px solid rgba(0, 212, 255, 0.3);
  border-radius: 24px;
  background: rgba(20, 20, 35, 0.65);
  color: #cbd5e0;
  transition: all 0.3s;
  font-family: 'Inter', sans-serif;
  box-shadow: 0 0 6px rgba(0, 212, 255, 0.1);
}

.preference-tag :deep(.ant-checkbox-wrapper:hover) {
  border-color: #00d4ff;
  background: rgba(0, 212, 255, 0.15);
  color: #fff;
  box-shadow: 0 0 12px rgba(0, 212, 255, 0.3);
}

.preference-tag :deep(.ant-checkbox-wrapper-checked) {
  border-color: #a855f7;
  background: linear-gradient(135deg, rgba(168, 85, 247, 0.4), rgba(0, 212, 255, 0.3));
  color: #fff;
  box-shadow: 0 0 14px rgba(168, 85, 247, 0.5);
  font-weight: 600;
}

/* 提交按钮 */
.submit-button {
  height: 64px;
  border-radius: 36px;
  font-size: 24px;
  font-weight: 700;
  font-family: 'Inter', sans-serif;
  background: linear-gradient(135deg, #00d4ff, #a855f7);
  border: none;
  box-shadow: 0 0 30px rgba(0, 212, 255, 0.5), 0 0 60px rgba(168, 85, 247, 0.3);
  color: #fff;
  letter-spacing: 2px;
  transition: all 0.3s;
  text-transform: uppercase;
}

.submit-button:hover {
  transform: translateY(-4px);
  box-shadow: 0 0 45px rgba(0, 212, 255, 0.75), 0 0 90px rgba(168, 85, 247, 0.6);
}

.submit-button:active {
  transform: translateY(0);
  box-shadow: 0 0 20px rgba(0, 212, 255, 0.4);
}

/* 加载区域 */
.loading-container {
  text-align: center;
  padding: 28px;
  background: rgba(20, 20, 35, 0.65);
  border-radius: 20px;
  backdrop-filter: blur(12px);
}

.loading-status {
  margin-top: 18px;
  color: #00d4ff;
  font-size: 18px;
  font-weight: 600;
  text-shadow: 0 0 10px rgba(0, 212, 255, 0.4);
}

/* 动画 */
@keyframes fadeInDown {
  from { opacity: 0; transform: translateY(-30px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
