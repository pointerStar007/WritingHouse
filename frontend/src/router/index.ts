import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import { useUserStore } from '@/stores/user'
import NProgress from 'nprogress'

// 路由配置
const routes: RouteRecordRaw[] = [
  {
    path: '/',
    redirect: '/dashboard'
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/auth/Login.vue'),
    meta: {
      title: '登录',
      requiresAuth: false
    }
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('@/views/auth/Register.vue'),
    meta: {
      title: '注册',
      requiresAuth: false
    }
  },
  {
    path: '/forgot-password',
    name: 'ForgotPassword',
    component: () => import('@/views/auth/ForgotPassword.vue'),
    meta: {
      title: '忘记密码',
      requiresAuth: false
    }
  },
  {
    path: '/',
    component: () => import('@/layouts/MainLayout.vue'),
    meta: {
      requiresAuth: true
    },
    children: [
      {
        path: 'dashboard',
        name: 'Dashboard',
        component: () => import('@/views/Dashboard.vue'),
        meta: {
          title: '仪表盘',
          icon: 'Dashboard'
        }
      },
      {
        path: 'works',
        name: 'Works',
        component: () => import('@/views/works/WorkList.vue'),
        meta: {
          title: '作品管理',
          icon: 'Document'
        }
      },
      {
        path: 'works/create',
        name: 'CreateWork',
        component: () => import('@/views/works/CreateWork.vue'),
        meta: {
          title: '创建作品',
          hidden: true
        }
      },
      {
        path: 'works/:id',
        name: 'WorkDetail',
        component: () => import('@/views/works/WorkDetail.vue'),
        meta: {
          title: '作品详情',
          hidden: true
        }
      },
      {
        path: 'works/:id/edit',
        name: 'WorkEdit',
        component: () => import('@/views/works/WorkEdit.vue'),
        meta: {
          title: '编辑作品',
          hidden: true
        }
      },
      {
        path: 'works/:workId/chapters/:id/edit',
        name: 'ChapterEdit',
        component: () => import('@/views/editor/ChapterEditor.vue'),
        meta: {
          title: '章节编辑',
          hidden: true
        }
      },
      {
        path: 'editor/chapter/:id',
        name: 'ChapterEditor',
        component: () => import('@/views/editor/ChapterEditor.vue'),
        meta: {
          title: '章节编辑器',
          hidden: true
        }
      },
      {
        path: 'statistics',
        name: 'Statistics',
        component: () => import('@/views/statistics/Statistics.vue'),
        meta: {
          title: '写作统计',
          icon: 'DataAnalysis'
        }
      },
      {
        path: 'statistics/daily',
        name: 'DailyStatistics',
        component: () => import('@/views/statistics/Statistics.vue'),
        meta: {
          title: '每日统计',
          hidden: true
        }
      },
      {
        path: 'statistics/goals',
        name: 'WritingGoals',
        component: () => import('@/views/statistics/Statistics.vue'),
        meta: {
          title: '写作目标',
          hidden: true
        }
      },
      {
        path: 'settings',
        name: 'Settings',
        component: () => import('@/views/settings/Settings.vue'),
        meta: {
          title: '设置',
          icon: 'Setting'
        }
      },
      {
        path: 'profile',
        name: 'Profile',
        component: () => import('@/views/profile/Profile.vue'),
        meta: {
          title: '个人资料',
          icon: 'User'
        }
      }
    ]
  },
  {
    path: '/preview/:workId',
    name: 'WorkPreview',
    component: () => import('@/views/preview/WorkPreview.vue'),
    meta: {
      title: '作品预览',
      requiresAuth: false
    }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/error/404.vue'),
    meta: {
      title: '页面不存在'
    }
  }
]

// 创建路由实例
const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

// 路由守卫
router.beforeEach(async (to, from, next) => {
  NProgress.start()
  
  const userStore = useUserStore()
  const isAuthenticated = userStore.isAuthenticated
  
  // 设置页面标题
  if (to.meta.title) {
    document.title = `${to.meta.title} - WritingHouse`
  } else {
    document.title = 'WritingHouse - 网络小说创作平台'
  }
  
  // 检查认证状态
  if (to.meta.requiresAuth !== false) {
    if (!isAuthenticated) {
      // 未登录，跳转到登录页
      next({ name: 'Login', query: { redirect: to.fullPath } })
      return
    }
    
    // 已登录但用户信息为空，尝试获取用户信息
    if (!userStore.user) {
      try {
        await userStore.fetchUserInfo()
      } catch (error) {
        // 获取用户信息失败，清除token并跳转到登录页
        userStore.logout()
        next({ name: 'Login', query: { redirect: to.fullPath } })
        return
      }
    }
  } else {
    // 不需要认证的页面，如果已登录则跳转到仪表盘
    if (isAuthenticated && (to.name === 'Login' || to.name === 'Register')) {
      next({ name: 'Dashboard' })
      return
    }
  }
  
  next()
})

router.afterEach(() => {
  NProgress.done()
})

export default router