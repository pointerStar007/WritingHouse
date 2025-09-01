<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { provide } from 'vue'
import { useDark, useToggle } from '@vueuse/core'

// 应用初始化逻辑
const { isDark } = useDark()
const toggleDark = useToggle(isDark)

// 提供全局主题切换
provide('toggleDark', toggleDark)
provide('isDark', isDark)
</script>

<style lang="scss">
#app {
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

// 全局滚动条样式
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: var(--el-bg-color-page);
}

::-webkit-scrollbar-thumb {
  background: var(--el-border-color-darker);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--el-border-color-dark);
}

// 暗色主题适配
.dark {
  color-scheme: dark;
}
</style>