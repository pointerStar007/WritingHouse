import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('@/views/auth/LoginView.vue'),
      meta: {
        requiresAuth: false,
        title: '登录 - WritingHouse'
      }
    },
    {
      path: '/register',
      name: 'Register',
      component: () => import('@/views/auth/RegisterView.vue'),
      meta: {
        requiresAuth: false,
        title: '注册 - WritingHouse'
      }
    },
    {
      path: '/forgot-password',
      name: 'ForgotPassword',
      component: () => import('@/views/auth/ForgotPasswordView.vue'),
      meta: {
        requiresAuth: false,
        title: '忘记密码 - WritingHouse'
      }
    },
    {
      path: '/home',
      name: 'Home',
      component: () => import('@/views/HomeView.vue'),
      meta: {
        requiresAuth: true,
        title: '首页 - WritingHouse'
      },
      children: [
        {
          path: '',
          redirect: '/home/dashboard'
        },
        {
          path: 'dashboard',
          name: 'Dashboard',
          component: () => import('@/views/dashboard/DashboardView.vue'),
          meta: {
            requiresAuth: true,
            title: '仪表盘 - WritingHouse'
          }
        },
        {
          path: 'works',
          name: 'Works',
          component: () => import('@/views/works/WorksView.vue'),
          meta: {
            requiresAuth: true,
            title: '作品管理 - WritingHouse'
          }
        },
        {
          path: 'works/:id',
          name: 'WorkDetail',
          component: () => import('@/views/works/WorkDetailView.vue'),
          meta: {
            requiresAuth: true,
            title: '作品详情 - WritingHouse'
          }
        },
        {
          path: 'works/:workId/volumes/:volumeId/chapters/:chapterId/edit',
          name: 'ChapterEdit',
          component: () => import('@/views/editor/ChapterEditView.vue'),
          meta: {
            requiresAuth: true,
            title: '章节编辑 - WritingHouse'
          }
        },
        {
          path: 'statistics',
          name: 'Statistics',
          component: () => import('@/views/statistics/StatisticsView.vue'),
          meta: {
            requiresAuth: true,
            title: '写作统计 - WritingHouse'
          }
        },
        {
          path: 'profile',
          name: 'Profile',
          component: () => import('@/views/profile/ProfileView.vue'),
          meta: {
            requiresAuth: true,
            title: '个人资料 - WritingHouse'
          }
        },
        {
          path: 'settings',
          name: 'Settings',
          component: () => import('@/views/settings/SettingsView.vue'),
          meta: {
            requiresAuth: true,
            title: '系统设置 - WritingHouse'
          }
        }
      ]
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: () => import('@/views/error/NotFoundView.vue'),
      meta: {
        requiresAuth: false,
        title: '页面未找到 - WritingHouse'
      }
    }
  ]
})

// 路由守卫
router.beforeEach(async (to, from, next) => {
  const userStore = useUserStore()
  
  // 设置页面标题
  if (to.meta.title) {
    document.title = to.meta.title as string
  }
  
  // 检查是否需要认证
  if (to.meta.requiresAuth) {
    // 检查用户是否已登录
    if (!userStore.isAuthenticated) {
      // 尝试从本地存储恢复用户状态
      await userStore.checkAuth()
      
      if (!userStore.isAuthenticated) {
        // 未登录，重定向到登录页
        next({
          name: 'Login',
          query: { redirect: to.fullPath }
        })
        return
      }
    }
  } else {
    // 如果已登录用户访问登录页，重定向到首页
    if (userStore.isAuthenticated && (to.name === 'Login' || to.name === 'Register')) {
      next({ name: 'Home' })
      return
    }
  }
  
  next()
})

export default router