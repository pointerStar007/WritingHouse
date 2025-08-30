<template>
  <div class="layout-container">
    <!-- 侧边栏 -->
    <aside class="sidebar" :class="{ collapsed: isCollapsed }">
      <div class="logo">
        <h2 v-if="!isCollapsed">写作小屋</h2>
        <h2 v-else>写</h2>
      </div>
      
      <nav class="nav-menu">
        <router-link
          v-for="item in menuItems"
          :key="item.path"
          :to="item.path"
          class="nav-item"
          :class="{ active: $route.path === item.path }"
        >
          <el-icon class="nav-icon">
            <component :is="item.icon" />
          </el-icon>
          <span v-if="!isCollapsed" class="nav-text">{{ item.title }}</span>
        </router-link>
      </nav>
    </aside>

    <!-- 主内容区 -->
    <div class="main-content">
      <!-- 顶部栏 -->
      <header class="header">
        <div class="header-left">
          <el-button
            type="text"
            @click="toggleSidebar"
            class="collapse-btn"
          >
            <el-icon><Fold v-if="!isCollapsed" /><Expand v-else /></el-icon>
          </el-button>
          <h1 class="page-title">{{ currentPageTitle }}</h1>
        </div>
        
        <div class="header-right">
          <el-dropdown>
            <div class="user-info">
              <el-avatar :size="32" src="/avatar.jpg" />
              <span class="username">作者</span>
            </div>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click="$router.push('/profile')">
                  个人中心
                </el-dropdown-item>
                <el-dropdown-item @click="$router.push('/settings')">
                  系统设置
                </el-dropdown-item>
                <el-dropdown-item divided>
                  退出登录
                </el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </header>

      <!-- 页面内容 -->
      <main class="page-content">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import {
  Dashboard,
  Document,
  Lightbulb,
  User,
  Setting,
  Fold,
  Expand
} from '@element-plus/icons-vue'

const route = useRoute()
const isCollapsed = ref(false)

// 菜单项配置
const menuItems = [
  {
    path: '/dashboard',
    title: '仪表盘',
    icon: 'Dashboard'
  },
  {
    path: '/works',
    title: '作品管理',
    icon: 'Document'
  },
  {
    path: '/inspirations',
    title: '灵感管理',
    icon: 'Lightbulb'
  },
  {
    path: '/profile',
    title: '个人中心',
    icon: 'User'
  },
  {
    path: '/settings',
    title: '系统设置',
    icon: 'Setting'
  }
]

// 当前页面标题
const currentPageTitle = computed(() => {
  const currentItem = menuItems.find(item => item.path === route.path)
  return currentItem?.title || '写作小屋'
})

// 切换侧边栏
const toggleSidebar = () => {
  isCollapsed.value = !isCollapsed.value
}
</script>

<style lang="scss" scoped>
.layout-container {
  display: flex;
  height: 100vh;
  background: #f5f7fa;
}

.sidebar {
  width: 250px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  transition: width 0.3s ease;
  display: flex;
  flex-direction: column;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);

  &.collapsed {
    width: 70px;
  }

  .logo {
    padding: 20px;
    text-align: center;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);

    h2 {
      margin: 0;
      font-size: 24px;
      font-weight: 600;
    }
  }

  .nav-menu {
    flex: 1;
    padding: 20px 0;

    .nav-item {
      display: flex;
      align-items: center;
      padding: 15px 20px;
      color: rgba(255, 255, 255, 0.8);
      text-decoration: none;
      transition: all 0.3s ease;
      border-left: 3px solid transparent;

      &:hover {
        background: rgba(255, 255, 255, 0.1);
        color: white;
      }

      &.active {
        background: rgba(255, 255, 255, 0.15);
        color: white;
        border-left-color: #fff;
      }

      .nav-icon {
        font-size: 20px;
        margin-right: 12px;
      }

      .nav-text {
        font-size: 16px;
        font-weight: 500;
      }
    }
  }
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.header {
  height: 60px;
  background: white;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  z-index: 100;

  .header-left {
    display: flex;
    align-items: center;

    .collapse-btn {
      margin-right: 15px;
      font-size: 18px;
    }

    .page-title {
      margin: 0;
      font-size: 20px;
      font-weight: 600;
      color: #303133;
    }
  }

  .header-right {
    .user-info {
      display: flex;
      align-items: center;
      cursor: pointer;
      padding: 5px 10px;
      border-radius: 20px;
      transition: background-color 0.3s ease;

      &:hover {
        background: #f5f7fa;
      }

      .username {
        margin-left: 8px;
        font-weight: 500;
        color: #606266;
      }
    }
  }
}

.page-content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  background: #f5f7fa;
}
</style>