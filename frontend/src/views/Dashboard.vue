<template>
  <div class="dashboard">
    <!-- 统计卡片 -->
    <div class="stats-grid">
      <div class="stat-card" v-for="stat in stats" :key="stat.title">
        <div class="stat-icon" :style="{ backgroundColor: stat.color }">
          <el-icon><component :is="stat.icon" /></el-icon>
        </div>
        <div class="stat-content">
          <h3>{{ stat.value }}</h3>
          <p>{{ stat.title }}</p>
        </div>
      </div>
    </div>

    <!-- 图表区域 -->
    <div class="charts-section">
      <div class="chart-card">
        <h3>写作趋势</h3>
        <div class="chart-container">
          <v-chart :option="trendOption" style="height: 300px;" />
        </div>
      </div>
      
      <div class="chart-card">
        <h3>作品分类</h3>
        <div class="chart-container">
          <v-chart :option="categoryOption" style="height: 300px;" />
        </div>
      </div>
    </div>

    <!-- 最近活动 -->
    <div class="recent-activity">
      <div class="card">
        <h3>最近活动</h3>
        <div class="activity-list">
          <div class="activity-item" v-for="activity in recentActivities" :key="activity.id">
            <div class="activity-icon">
              <el-icon><component :is="activity.icon" /></el-icon>
            </div>
            <div class="activity-content">
              <p>{{ activity.content }}</p>
              <span class="activity-time">{{ activity.time }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { LineChart, PieChart } from 'echarts/charts'
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
} from 'echarts/components'
import VChart from 'vue-echarts'
import {
  Document,
  Lightbulb,
  Clock,
  TrendCharts,
  Edit,
  Plus
} from '@element-plus/icons-vue'

use([
  CanvasRenderer,
  LineChart,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
])

// 统计数据
const stats = ref([
  {
    title: '总作品数',
    value: '12',
    icon: 'Document',
    color: '#409eff'
  },
  {
    title: '灵感记录',
    value: '48',
    icon: 'Lightbulb',
    color: '#67c23a'
  },
  {
    title: '今日字数',
    value: '2,580',
    icon: 'Edit',
    color: '#e6a23c'
  },
  {
    title: '写作时长',
    value: '3.5h',
    icon: 'Clock',
    color: '#f56c6c'
  }
])

// 趋势图配置
const trendOption = ref({
  tooltip: {
    trigger: 'axis'
  },
  xAxis: {
    type: 'category',
    data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
  },
  yAxis: {
    type: 'value'
  },
  series: [{
    data: [1200, 1900, 3000, 5000, 2300, 2200, 3200],
    type: 'line',
    smooth: true,
    itemStyle: {
      color: '#667eea'
    },
    areaStyle: {
      color: {
        type: 'linear',
        x: 0,
        y: 0,
        x2: 0,
        y2: 1,
        colorStops: [{
          offset: 0, color: 'rgba(102, 126, 234, 0.3)'
        }, {
          offset: 1, color: 'rgba(102, 126, 234, 0.1)'
        }]
      }
    }
  }]
})

// 分类饼图配置
const categoryOption = ref({
  tooltip: {
    trigger: 'item'
  },
  legend: {
    orient: 'vertical',
    left: 'left'
  },
  series: [{
    type: 'pie',
    radius: '50%',
    data: [
      { value: 5, name: '小说' },
      { value: 3, name: '散文' },
      { value: 2, name: '诗歌' },
      { value: 2, name: '随笔' }
    ],
    emphasis: {
      itemStyle: {
        shadowBlur: 10,
        shadowOffsetX: 0,
        shadowColor: 'rgba(0, 0, 0, 0.5)'
      }
    }
  }]
})

// 最近活动
const recentActivities = ref([
  {
    id: 1,
    content: '创建了新作品《春天的故事》',
    time: '2小时前',
    icon: 'Plus'
  },
  {
    id: 2,
    content: '更新了作品《夏日回忆》第三章',
    time: '5小时前',
    icon: 'Edit'
  },
  {
    id: 3,
    content: '记录了新的创作灵感',
    time: '1天前',
    icon: 'Lightbulb'
  },
  {
    id: 4,
    content: '完成了今日写作目标',
    time: '2天前',
    icon: 'TrendCharts'
  }
])

onMounted(() => {
  // 组件挂载后的逻辑
})
</script>

<style lang="scss" scoped>
.dashboard {
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-bottom: 30px;

    .stat-card {
      background: white;
      border-radius: 12px;
      padding: 24px;
      display: flex;
      align-items: center;
      box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease;

      &:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
      }

      .stat-icon {
        width: 60px;
        height: 60px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 16px;
        color: white;
        font-size: 24px;
      }

      .stat-content {
        h3 {
          font-size: 28px;
          font-weight: 700;
          color: #303133;
          margin: 0 0 4px 0;
        }

        p {
          font-size: 14px;
          color: #909399;
          margin: 0;
        }
      }
    }
  }

  .charts-section {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-bottom: 30px;

    .chart-card {
      background: white;
      border-radius: 12px;
      padding: 24px;
      box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);

      h3 {
        margin: 0 0 20px 0;
        font-size: 18px;
        font-weight: 600;
        color: #303133;
      }

      .chart-container {
        width: 100%;
      }
    }
  }

  .recent-activity {
    .card {
      h3 {
        margin: 0 0 20px 0;
        font-size: 18px;
        font-weight: 600;
        color: #303133;
      }

      .activity-list {
        .activity-item {
          display: flex;
          align-items: center;
          padding: 16px 0;
          border-bottom: 1px solid #f0f0f0;

          &:last-child {
            border-bottom: none;
          }

          .activity-icon {
            width: 40px;
            height: 40px;
            border-radius: 8px;
            background: #f5f7fa;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 12px;
            color: #409eff;
            font-size: 16px;
          }

          .activity-content {
            flex: 1;

            p {
              margin: 0 0 4px 0;
              font-size: 14px;
              color: #303133;
            }

            .activity-time {
              font-size: 12px;
              color: #909399;
            }
          }
        }
      }
    }
  }
}

@media (max-width: 768px) {
  .dashboard {
    .stats-grid {
      grid-template-columns: 1fr;
    }

    .charts-section {
      grid-template-columns: 1fr;
    }
  }
}
</style>