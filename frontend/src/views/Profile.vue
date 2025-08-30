<template>
  <div class="profile">
    <!-- 个人信息卡片 -->
    <div class="profile-card">
      <div class="profile-header">
        <div class="avatar-section">
          <el-avatar :size="120" :src="userInfo.avatar" />
          <el-button type="primary" size="small" class="upload-btn">
            <el-icon><Camera /></el-icon>
            更换头像
          </el-button>
        </div>
        
        <div class="info-section">
          <h2>{{ userInfo.name }}</h2>
          <p class="bio">{{ userInfo.bio }}</p>
          
          <div class="social-links">
            <el-button 
              v-for="link in userInfo.socialLinks" 
              :key="link.platform"
              type="text"
              @click="openLink(link.url)"
            >
              <el-icon><component :is="link.icon" /></el-icon>
              {{ link.platform }}
            </el-button>
          </div>
        </div>
      </div>
      
      <div class="profile-stats">
        <div class="stat-item">
          <h3>{{ stats.totalWorks }}</h3>
          <p>总作品数</p>
        </div>
        <div class="stat-item">
          <h3>{{ stats.totalWords }}</h3>
          <p>总字数</p>
        </div>
        <div class="stat-item">
          <h3>{{ stats.writingDays }}</h3>
          <p>写作天数</p>
        </div>
        <div class="stat-item">
          <h3>{{ stats.inspirations }}</h3>
          <p>灵感记录</p>
        </div>
      </div>
    </div>

    <!-- 写作成就 -->
    <div class="achievements-section">
      <h3>写作成就</h3>
      <div class="achievements-grid">
        <div 
          class="achievement-item" 
          v-for="achievement in achievements" 
          :key="achievement.id"
          :class="{ unlocked: achievement.unlocked }"
        >
          <div class="achievement-icon">
            <el-icon><component :is="achievement.icon" /></el-icon>
          </div>
          <div class="achievement-info">
            <h4>{{ achievement.title }}</h4>
            <p>{{ achievement.description }}</p>
            <div class="achievement-progress" v-if="!achievement.unlocked">
              <el-progress 
                :percentage="achievement.progress" 
                :show-text="false" 
                :stroke-width="4"
              />
              <span class="progress-text">{{ achievement.current }}/{{ achievement.target }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 最近作品 -->
    <div class="recent-works-section">
      <h3>最近作品</h3>
      <div class="works-list">
        <div 
          class="work-item" 
          v-for="work in recentWorks" 
          :key="work.id"
        >
          <div class="work-cover">
            <img :src="work.cover || '/default-cover.jpg'" :alt="work.title" />
          </div>
          <div class="work-info">
            <h4>{{ work.title }}</h4>
            <p>{{ work.description }}</p>
            <div class="work-meta">
              <span class="work-category">{{ getCategoryText(work.category) }}</span>
              <span class="work-words">{{ work.wordCount }} 字</span>
              <span class="work-date">{{ formatDate(work.updatedAt) }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import {
  Camera,
  Trophy,
  Medal,
  Star,
  Crown,
  Link
} from '@element-plus/icons-vue'

// 用户信息
const userInfo = ref({
  name: '创作者',
  bio: '热爱文字，用心创作每一个故事',
  avatar: '/avatar.jpg',
  socialLinks: [
    {
      platform: '微博',
      url: 'https://weibo.com',
      icon: 'Link'
    },
    {
      platform: '知乎',
      url: 'https://zhihu.com',
      icon: 'Link'
    }
  ]
})

// 统计数据
const stats = ref({
  totalWorks: 12,
  totalWords: '156,789',
  writingDays: 365,
  inspirations: 48
})

// 成就系统
const achievements = ref([
  {
    id: 1,
    title: '初出茅庐',
    description: '完成第一部作品',
    icon: 'Star',
    unlocked: true,
    progress: 100,
    current: 1,
    target: 1
  },
  {
    id: 2,
    title: '勤奋写手',
    description: '连续写作30天',
    icon: 'Medal',
    unlocked: true,
    progress: 100,
    current: 30,
    target: 30
  },
  {
    id: 3,
    title: '字数达人',
    description: '累计写作10万字',
    icon: 'Trophy',
    unlocked: false,
    progress: 78,
    current: 78000,
    target: 100000
  },
  {
    id: 4,
    title: '创作大师',
    description: '完成20部作品',
    icon: 'Crown',
    unlocked: false,
    progress: 60,
    current: 12,
    target: 20
  }
])

// 最近作品
const recentWorks = ref([
  {
    id: 1,
    title: '春天的故事',
    description: '一个关于成长和希望的温暖故事',
    category: 'novel',
    wordCount: 15000,
    cover: '',
    updatedAt: '2024-01-20'
  },
  {
    id: 2,
    title: '夏日回忆',
    description: '童年夏天的美好回忆',
    category: 'essay',
    wordCount: 8500,
    cover: '',
    updatedAt: '2024-01-18'
  },
  {
    id: 3,
    title: '秋叶飘零',
    description: '描写秋天景色的诗歌集',
    category: 'poetry',
    wordCount: 2300,
    cover: '',
    updatedAt: '2024-01-12'
  }
])

// 获取分类文本
const getCategoryText = (category: string) => {
  const categoryMap: Record<string, string> = {
    novel: '小说',
    essay: '散文',
    poetry: '诗歌',
    note: '随笔'
  }
  return categoryMap[category] || category
}

// 格式化日期
const formatDate = (dateStr: string) => {
  const date = new Date(dateStr)
  return date.toLocaleDateString('zh-CN')
}

// 打开链接
const openLink = (url: string) => {
  window.open(url, '_blank')
}

onMounted(() => {
  // 组件挂载后的逻辑
})
</script>

<style lang="scss" scoped>
.profile {
  .profile-card {
    background: white;
    border-radius: 16px;
    padding: 30px;
    margin-bottom: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);

    .profile-header {
      display: flex;
      gap: 30px;
      margin-bottom: 30px;

      .avatar-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 16px;

        .upload-btn {
          font-size: 12px;
        }
      }

      .info-section {
        flex: 1;

        h2 {
          margin: 0 0 12px 0;
          font-size: 28px;
          font-weight: 600;
          color: #303133;
        }

        .bio {
          margin: 0 0 20px 0;
          color: #606266;
          font-size: 16px;
          line-height: 1.6;
        }

        .social-links {
          display: flex;
          gap: 12px;
        }
      }
    }

    .profile-stats {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      padding-top: 30px;
      border-top: 1px solid #f0f0f0;

      .stat-item {
        text-align: center;

        h3 {
          margin: 0 0 8px 0;
          font-size: 24px;
          font-weight: 700;
          color: #409eff;
        }

        p {
          margin: 0;
          color: #909399;
          font-size: 14px;
        }
      }
    }
  }

  .achievements-section,
  .recent-works-section {
    background: white;
    border-radius: 16px;
    padding: 30px;
    margin-bottom: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);

    h3 {
      margin: 0 0 24px 0;
      font-size: 20px;
      font-weight: 600;
      color: #303133;
    }
  }

  .achievements-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;

    .achievement-item {
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 20px;
      border: 2px solid #f0f0f0;
      border-radius: 12px;
      transition: all 0.3s ease;

      &.unlocked {
        border-color: #67c23a;
        background: #f0f9ff;

        .achievement-icon {
          background: #67c23a;
          color: white;
        }
      }

      .achievement-icon {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: #f0f0f0;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        color: #909399;
      }

      .achievement-info {
        flex: 1;

        h4 {
          margin: 0 0 4px 0;
          font-size: 16px;
          font-weight: 600;
          color: #303133;
        }

        p {
          margin: 0 0 8px 0;
          color: #606266;
          font-size: 14px;
        }

        .achievement-progress {
          display: flex;
          align-items: center;
          gap: 12px;

          .el-progress {
            flex: 1;
          }

          .progress-text {
            font-size: 12px;
            color: #909399;
            white-space: nowrap;
          }
        }
      }
    }
  }

  .works-list {
    display: flex;
    flex-direction: column;
    gap: 16px;

    .work-item {
      display: flex;
      gap: 16px;
      padding: 16px;
      border: 1px solid #f0f0f0;
      border-radius: 8px;
      transition: all 0.3s ease;

      &:hover {
        border-color: #409eff;
        box-shadow: 0 2px 8px rgba(64, 158, 255, 0.1);
      }

      .work-cover {
        width: 60px;
        height: 80px;
        border-radius: 4px;
        overflow: hidden;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 20px;

        img {
          width: 100%;
          height: 100%;
          object-fit: cover;
        }
      }

      .work-info {
        flex: 1;

        h4 {
          margin: 0 0 8px 0;
          font-size: 16px;
          font-weight: 600;
          color: #303133;
        }

        p {
          margin: 0 0 12px 0;
          color: #606266;
          font-size: 14px;
          line-height: 1.5;
        }

        .work-meta {
          display: flex;
          gap: 16px;
          font-size: 12px;
          color: #909399;

          .work-category {
            background: #f0f9ff;
            color: #0369a1;
            padding: 2px 6px;
            border-radius: 8px;
          }
        }
      }
    }
  }
}

@media (max-width: 768px) {
  .profile {
    .profile-card {
      .profile-header {
        flex-direction: column;
        text-align: center;
      }

      .profile-stats {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    .achievements-grid {
      grid-template-columns: 1fr;
    }
  }
}
</style>