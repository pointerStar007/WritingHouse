<template>
  <header class="app-header">
    <div class="header-container">
      <!-- Logo和标题 -->
      <div class="header-left">
        <router-link to="/" class="logo-link">
          <div class="logo">
            <el-icon size="32"><EditPen /></el-icon>
          </div>
          <h1>写作小屋</h1>
        </router-link>
      </div>

      <!-- 导航菜单 -->
      <nav class="header-nav">
        <router-link 
          v-for="item in navItems" 
          :key="item.path"
          :to="item.path"
          class="nav-item"
          :class="{ active: $route.path === item.path }"
        >
          <el-icon><component :is="item.icon" /></el-icon>
          <span>{{ item.name }}</span>
        </router-link>
      </nav>

      <!-- 用户操作区 -->
      <div class="header-right">
        <!-- 搜索框 -->
        <div class="search-box">
          <el-input
            v-model="searchText"
            placeholder="搜索作品或灵感..."
            size="small"
            style="width: 200px;"
            clearable
            @keyup.enter="handleSearch"
          >
            <template #prefix>
              <el-icon><Search /></el-icon>
            </template>
          </el-input>
        </div>

        <!-- 通知 -->
        <el-badge :value="notificationCount" :hidden="notificationCount === 0">
          <el-button type="text" @click="showNotifications">
            <el-icon size="20"><Bell /></el-icon>
          </el-button>
        </el-badge>

        <!-- 用户菜单 -->
        <el-dropdown @command="handleUserCommand">
          <div class="user-info">
            <el-avatar :size="32" :src="userInfo.avatar" />
            <span class="username">{{ userInfo.name }}</span>
            <el-icon><ArrowDown /></el-icon>
          </div>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item command="profile">
                <el-icon><User /></el-icon>
                个人中心
              </el-dropdown-item>
              <el-dropdown-item command="settings">
                <el-icon><Setting /></el-icon>
                设置
              </el-dropdown-item>
              <el-dropdown-item divided command="logout">
                <el-icon><SwitchButton /></el-icon>
                退出登录
              </el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import {
  EditPen,
  Search,
  Bell,
  User,
  Setting,
  SwitchButton,
  ArrowDown,
  House,
  Document,
  Lightbulb
} from '@element-plus/icons-vue'

const router = useRouter()

// 搜索文本
const searchText = ref('')

// 导航菜单项
const navItems = [
  { name: '仪表盘', path: '/', icon: 'House' },
  { name: '作品管理', path: '/works', icon: 'Document' },
  { name: '灵感管理', path: '/inspirations', icon: 'Lightbulb' },
  { name: '个人中心', path: '/profile', icon: 'User' }
]

// 用户信息
const userInfo = ref({
  name: '创作者',
  avatar: '/avatar.jpg'
})

// 通知数量
const notificationCount = ref(3)

// 处理搜索
const handleSearch = () => {
  if (searchText.value.trim()) {
    ElMessage.info(`搜索：${searchText.value}`)
    // 这里可以实现搜索逻辑
  }
}

// 显示通知
const showNotifications = () => {
  ElMessage.info('显示通知列表')
  // 这里可以打开通知面板
}

// 处理用户菜单命令
const handleUserCommand = (command: string) => {
  switch (command) {
    case 'profile':
      router.push('/profile')
      break
    case 'settings':
      ElMessage.info('打开设置')
      break
    case 'logout':
      ElMessage.success('已退出登录')
      // 这里可以实现退出登录逻辑
      break
  }
}
</script>

<style lang="scss" scoped>
.app-header {
  background: white;
  border-bottom: 1px solid #e4e7ed;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 1000;

  .header-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 24px;
    height: 64px;
    max-width: 1200px;
    margin: 0 auto;
  }

  .header-left {
    .logo-link {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;

      .logo {
        color: #409eff;
      }

      h1 {
        margin: 0;
        font-size: 20px;
        font-weight: 600;
        color: #303133;
      }
    }
  }

  .header-nav {
    display: flex;
    gap: 8px;

    .nav-item {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      border-radius: 8px;
      text-decoration: none;
      color: #606266;
      font-size: 14px;
      transition: all 0.3s ease;

      &:hover {
        background: #f5f7fa;
        color: #409eff;
      }

      &.active {
        background: #ecf5ff;
        color: #409eff;
        font-weight: 500;
      }
    }
  }

  .header-right {
    display: flex;
    align-items: center;
    gap: 16px;

    .search-box {
      .el-input {
        :deep(.el-input__wrapper) {
          border-radius: 20px;
        }
      }
    }

    .user-info {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 4px 8px;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.3s ease;

      &:hover {
        background: #f5f7fa;
      }

      .username {
        font-size: 14px;
        color: #303133;
      }
    }
  }
}

@media (max-width: 768px) {
  .app-header {
    .header-container {
      padding: 0 16px;
    }

    .header-nav {
      display: none;
    }

    .search-box {
      display: none;
    }
  }
}
</style>