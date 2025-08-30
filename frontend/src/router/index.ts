import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import NProgress from 'nprogress'

// 导入布局组件
import Layout from '@/layouts/Layout.vue'

// 路由配置
const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
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
        component: () => import('@/views/Works.vue'),
        meta: {
          title: '作品管理',
          icon: 'Document'
        }
      },
      {
        path: 'inspirations',
        name: 'Inspirations',
        component: () => import('@/views/Inspirations.vue'),
        meta: {
          title: '灵感管理',
          icon: 'Lightbulb'
        }
      },
      {
        path: 'profile',
        name: 'Profile',
        component: () => import('@/views/Profile.vue'),
        meta: {
          title: '个人中心',
          icon: 'User'
        }
      },
      {
        path: 'settings',
        name: 'Settings',
        component: () => import('@/views/Settings.vue'),
        meta: {
          title: '系统设置',
          icon: 'Setting'
        }
      }
    ]
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/404.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫
router.beforeEach((to, from, next) => {
  NProgress.start()
  
  // 设置页面标题
  if (to.meta?.title) {
    document.title = `${to.meta.title} - 写作小屋`
  } else {
    document.title = '写作小屋 - 现代化写作管理平台'
  }
  
  next()
})

router.afterEach(() => {
  NProgress.done()
})

export default router