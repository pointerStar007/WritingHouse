<template>
  <div class="inspirations">
    <!-- 页面头部 -->
    <div class="page-header">
      <div class="header-left">
        <h2>灵感管理</h2>
        <p>记录和管理您的创作灵感</p>
      </div>
      <div class="header-right">
        <el-button type="primary" @click="showCreateDialog = true">
          <el-icon><Plus /></el-icon>
          记录灵感
        </el-button>
      </div>
    </div>

    <!-- 筛选栏 -->
    <div class="filter-bar">
      <el-input
        v-model="searchText"
        placeholder="搜索灵感..."
        style="width: 300px;"
        clearable
      >
        <template #prefix>
          <el-icon><Search /></el-icon>
        </template>
      </el-input>
      
      <el-select v-model="tagFilter" placeholder="标签筛选" style="width: 120px;">
        <el-option label="全部" value="" />
        <el-option label="人物" value="character" />
        <el-option label="情节" value="plot" />
        <el-option label="场景" value="scene" />
        <el-option label="对话" value="dialogue" />
      </el-select>
    </div>

    <!-- 灵感列表 -->
    <div class="inspirations-grid">
      <div 
        class="inspiration-card" 
        v-for="inspiration in filteredInspirations" 
        :key="inspiration.id"
      >
        <div class="inspiration-header">
          <div class="inspiration-tag" :class="inspiration.tag">
            {{ getTagText(inspiration.tag) }}
          </div>
          <div class="inspiration-actions">
            <el-button size="small" type="text" @click="editInspiration(inspiration)">
              <el-icon><Edit /></el-icon>
            </el-button>
            <el-button size="small" type="text" @click="deleteInspiration(inspiration)">
              <el-icon><Delete /></el-icon>
            </el-button>
          </div>
        </div>
        
        <div class="inspiration-content">
          <h3>{{ inspiration.title }}</h3>
          <p>{{ inspiration.content }}</p>
        </div>
        
        <div class="inspiration-footer">
          <span class="inspiration-date">{{ formatDate(inspiration.createdAt) }}</span>
          <el-button size="small" @click="convertToWork(inspiration)">
            转为作品
          </el-button>
        </div>
      </div>
    </div>

    <!-- 新建灵感对话框 -->
    <el-dialog v-model="showCreateDialog" title="记录灵感" width="500px">
      <el-form :model="newInspiration" label-width="80px">
        <el-form-item label="灵感标题">
          <el-input v-model="newInspiration.title" placeholder="请输入灵感标题" />
        </el-form-item>
        
        <el-form-item label="灵感内容">
          <el-input 
            v-model="newInspiration.content" 
            type="textarea" 
            :rows="5"
            placeholder="请输入灵感内容"
          />
        </el-form-item>
        
        <el-form-item label="标签分类">
          <el-select v-model="newInspiration.tag" placeholder="请选择标签">
            <el-option label="人物" value="character" />
            <el-option label="情节" value="plot" />
            <el-option label="场景" value="scene" />
            <el-option label="对话" value="dialogue" />
          </el-select>
        </el-form-item>
      </el-form>
      
      <template #footer>
        <el-button @click="showCreateDialog = false">取消</el-button>
        <el-button type="primary" @click="createInspiration">保存</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import {
  Plus,
  Search,
  Edit,
  Delete
} from '@element-plus/icons-vue'

// 响应式数据
const searchText = ref('')
const tagFilter = ref('')
const showCreateDialog = ref(false)

// 新建灵感表单
const newInspiration = ref({
  title: '',
  content: '',
  tag: ''
})

// 灵感列表数据
const inspirations = ref([
  {
    id: 1,
    title: '神秘的老人',
    content: '在公园里遇到一个神秘的老人，他总是在同一个时间出现，手里拿着一本古老的书...',
    tag: 'character',
    createdAt: '2024-01-20'
  },
  {
    id: 2,
    title: '雨夜的咖啡店',
    content: '一个下雨的夜晚，咖啡店里只有一个客人，窗外的雨声和店内的音乐形成了奇妙的对比...',
    tag: 'scene',
    createdAt: '2024-01-19'
  },
  {
    id: 3,
    title: '时间旅行者的困境',
    content: '如果一个人可以回到过去，但每次回去都会改变现在，他应该如何选择？',
    tag: 'plot',
    createdAt: '2024-01-18'
  },
  {
    id: 4,
    title: '母亲的话',
    content: '"孩子，记住，真正的勇气不是不害怕，而是即使害怕也要去做正确的事。"',
    tag: 'dialogue',
    createdAt: '2024-01-17'
  }
])

// 筛选后的灵感列表
const filteredInspirations = computed(() => {
  return inspirations.value.filter(inspiration => {
    const matchesSearch = inspiration.title.toLowerCase().includes(searchText.value.toLowerCase()) ||
                         inspiration.content.toLowerCase().includes(searchText.value.toLowerCase())
    const matchesTag = !tagFilter.value || inspiration.tag === tagFilter.value
    
    return matchesSearch && matchesTag
  })
})

// 获取标签文本
const getTagText = (tag: string) => {
  const tagMap: Record<string, string> = {
    character: '人物',
    plot: '情节',
    scene: '场景',
    dialogue: '对话'
  }
  return tagMap[tag] || tag
}

// 格式化日期
const formatDate = (dateStr: string) => {
  const date = new Date(dateStr)
  return date.toLocaleDateString('zh-CN')
}

// 编辑灵感
const editInspiration = (inspiration: any) => {
  ElMessage.info(`编辑灵感：${inspiration.title}`)
  // 这里可以打开编辑对话框
}

// 删除灵感
const deleteInspiration = async (inspiration: any) => {
  try {
    await ElMessageBox.confirm(
      `确定要删除灵感「${inspiration.title}」吗？`,
      '确认删除',
      {
        confirmButtonText: '删除',
        cancelButtonText: '取消',
        type: 'warning'
      }
    )
    
    // 执行删除操作
    const index = inspirations.value.findIndex(i => i.id === inspiration.id)
    if (index > -1) {
      inspirations.value.splice(index, 1)
      ElMessage.success('删除成功')
    }
  } catch {
    // 用户取消删除
  }
}

// 转为作品
const convertToWork = (inspiration: any) => {
  ElMessage.success(`灵感「${inspiration.title}」已转为作品`)
  // 这里可以跳转到新建作品页面，并预填充内容
}

// 创建灵感
const createInspiration = () => {
  if (!newInspiration.value.title.trim()) {
    ElMessage.warning('请输入灵感标题')
    return
  }
  
  if (!newInspiration.value.content.trim()) {
    ElMessage.warning('请输入灵感内容')
    return
  }
  
  if (!newInspiration.value.tag) {
    ElMessage.warning('请选择标签分类')
    return
  }
  
  // 创建新灵感
  const inspiration = {
    id: Date.now(),
    title: newInspiration.value.title,
    content: newInspiration.value.content,
    tag: newInspiration.value.tag,
    createdAt: new Date().toISOString().split('T')[0]
  }
  
  inspirations.value.unshift(inspiration)
  
  // 重置表单
  newInspiration.value = {
    title: '',
    content: '',
    tag: ''
  }
  
  showCreateDialog.value = false
  ElMessage.success('灵感记录成功')
}

onMounted(() => {
  // 组件挂载后的逻辑
})
</script>

<style lang="scss" scoped>
.inspirations {
  .page-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
    padding: 20px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);

    .header-left {
      h2 {
        margin: 0 0 8px 0;
        font-size: 24px;
        font-weight: 600;
        color: #303133;
      }

      p {
        margin: 0;
        color: #909399;
        font-size: 14px;
      }
    }
  }

  .filter-bar {
    display: flex;
    gap: 16px;
    margin-bottom: 20px;
    padding: 20px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  }

  .inspirations-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 20px;

    .inspiration-card {
      background: white;
      border-radius: 12px;
      padding: 20px;
      box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
      transition: all 0.3s ease;

      &:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
      }

      .inspiration-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 16px;

        .inspiration-tag {
          padding: 4px 12px;
          border-radius: 16px;
          font-size: 12px;
          font-weight: 500;
          color: white;

          &.character {
            background: #409eff;
          }

          &.plot {
            background: #67c23a;
          }

          &.scene {
            background: #e6a23c;
          }

          &.dialogue {
            background: #f56c6c;
          }
        }

        .inspiration-actions {
          display: flex;
          gap: 4px;
        }
      }

      .inspiration-content {
        margin-bottom: 16px;

        h3 {
          margin: 0 0 12px 0;
          font-size: 16px;
          font-weight: 600;
          color: #303133;
        }

        p {
          margin: 0;
          color: #606266;
          font-size: 14px;
          line-height: 1.6;
          display: -webkit-box;
          -webkit-line-clamp: 3;
          -webkit-box-orient: vertical;
          overflow: hidden;
        }
      }

      .inspiration-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-top: 16px;
        border-top: 1px solid #f0f0f0;

        .inspiration-date {
          color: #909399;
          font-size: 12px;
        }
      }
    }
  }
}

@media (max-width: 768px) {
  .inspirations {
    .page-header {
      flex-direction: column;
      align-items: flex-start;
      gap: 16px;
    }

    .filter-bar {
      flex-direction: column;
    }

    .inspirations-grid {
      grid-template-columns: 1fr;
    }
  }
}
</style>