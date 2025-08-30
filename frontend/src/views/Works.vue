<template>
  <div class="works">
    <!-- 页面头部 -->
    <div class="page-header">
      <div class="header-left">
        <h2>作品管理</h2>
        <p>管理您的所有创作作品</p>
      </div>
      <div class="header-right">
        <el-button type="primary" @click="showCreateDialog = true">
          <el-icon><Plus /></el-icon>
          新建作品
        </el-button>
      </div>
    </div>

    <!-- 筛选栏 -->
    <div class="filter-bar">
      <el-input
        v-model="searchText"
        placeholder="搜索作品..."
        style="width: 300px;"
        clearable
      >
        <template #prefix>
          <el-icon><Search /></el-icon>
        </template>
      </el-input>
      
      <el-select v-model="statusFilter" placeholder="状态筛选" style="width: 120px;">
        <el-option label="全部" value="" />
        <el-option label="草稿" value="draft" />
        <el-option label="进行中" value="writing" />
        <el-option label="已完成" value="completed" />
      </el-select>
      
      <el-select v-model="categoryFilter" placeholder="分类筛选" style="width: 120px;">
        <el-option label="全部" value="" />
        <el-option label="小说" value="novel" />
        <el-option label="散文" value="essay" />
        <el-option label="诗歌" value="poetry" />
        <el-option label="随笔" value="note" />
      </el-select>
    </div>

    <!-- 作品列表 -->
    <div class="works-grid">
      <div 
        class="work-card" 
        v-for="work in filteredWorks" 
        :key="work.id"
        @click="openWork(work)"
      >
        <div class="work-cover">
          <img :src="work.cover || '/default-cover.jpg'" :alt="work.title" />
          <div class="work-status" :class="work.status">
            {{ getStatusText(work.status) }}
          </div>
        </div>
        
        <div class="work-info">
          <h3>{{ work.title }}</h3>
          <p class="work-description">{{ work.description }}</p>
          
          <div class="work-meta">
            <span class="work-category">{{ getCategoryText(work.category) }}</span>
            <span class="work-words">{{ work.wordCount }} 字</span>
          </div>
          
          <div class="work-footer">
            <span class="work-date">{{ formatDate(work.updatedAt) }}</span>
            <div class="work-actions">
              <el-button size="small" type="text" @click.stop="editWork(work)">
                <el-icon><Edit /></el-icon>
              </el-button>
              <el-button size="small" type="text" @click.stop="deleteWork(work)">
                <el-icon><Delete /></el-icon>
              </el-button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 新建作品对话框 -->
    <el-dialog v-model="showCreateDialog" title="新建作品" width="500px">
      <el-form :model="newWork" label-width="80px">
        <el-form-item label="作品标题">
          <el-input v-model="newWork.title" placeholder="请输入作品标题" />
        </el-form-item>
        
        <el-form-item label="作品描述">
          <el-input 
            v-model="newWork.description" 
            type="textarea" 
            :rows="3"
            placeholder="请输入作品描述"
          />
        </el-form-item>
        
        <el-form-item label="作品分类">
          <el-select v-model="newWork.category" placeholder="请选择分类">
            <el-option label="小说" value="novel" />
            <el-option label="散文" value="essay" />
            <el-option label="诗歌" value="poetry" />
            <el-option label="随笔" value="note" />
          </el-select>
        </el-form-item>
      </el-form>
      
      <template #footer>
        <el-button @click="showCreateDialog = false">取消</el-button>
        <el-button type="primary" @click="createWork">创建</el-button>
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
const statusFilter = ref('')
const categoryFilter = ref('')
const showCreateDialog = ref(false)

// 新建作品表单
const newWork = ref({
  title: '',
  description: '',
  category: ''
})

// 作品列表数据
const works = ref([
  {
    id: 1,
    title: '春天的故事',
    description: '一个关于成长和希望的温暖故事',
    category: 'novel',
    status: 'writing',
    wordCount: 15000,
    cover: '',
    createdAt: '2024-01-15',
    updatedAt: '2024-01-20'
  },
  {
    id: 2,
    title: '夏日回忆',
    description: '童年夏天的美好回忆',
    category: 'essay',
    status: 'completed',
    wordCount: 8500,
    cover: '',
    createdAt: '2024-01-10',
    updatedAt: '2024-01-18'
  },
  {
    id: 3,
    title: '秋叶飘零',
    description: '描写秋天景色的诗歌集',
    category: 'poetry',
    status: 'draft',
    wordCount: 2300,
    cover: '',
    createdAt: '2024-01-05',
    updatedAt: '2024-01-12'
  }
])

// 筛选后的作品列表
const filteredWorks = computed(() => {
  return works.value.filter(work => {
    const matchesSearch = work.title.toLowerCase().includes(searchText.value.toLowerCase()) ||
                         work.description.toLowerCase().includes(searchText.value.toLowerCase())
    const matchesStatus = !statusFilter.value || work.status === statusFilter.value
    const matchesCategory = !categoryFilter.value || work.category === categoryFilter.value
    
    return matchesSearch && matchesStatus && matchesCategory
  })
})

// 获取状态文本
const getStatusText = (status: string) => {
  const statusMap: Record<string, string> = {
    draft: '草稿',
    writing: '进行中',
    completed: '已完成'
  }
  return statusMap[status] || status
}

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

// 打开作品
const openWork = (work: any) => {
  ElMessage.info(`打开作品：${work.title}`)
  // 这里可以跳转到作品编辑页面
}

// 编辑作品
const editWork = (work: any) => {
  ElMessage.info(`编辑作品：${work.title}`)
  // 这里可以打开编辑对话框或跳转到编辑页面
}

// 删除作品
const deleteWork = async (work: any) => {
  try {
    await ElMessageBox.confirm(
      `确定要删除作品「${work.title}」吗？此操作不可恢复。`,
      '确认删除',
      {
        confirmButtonText: '删除',
        cancelButtonText: '取消',
        type: 'warning'
      }
    )
    
    // 执行删除操作
    const index = works.value.findIndex(w => w.id === work.id)
    if (index > -1) {
      works.value.splice(index, 1)
      ElMessage.success('删除成功')
    }
  } catch {
    // 用户取消删除
  }
}

// 创建作品
const createWork = () => {
  if (!newWork.value.title.trim()) {
    ElMessage.warning('请输入作品标题')
    return
  }
  
  if (!newWork.value.category) {
    ElMessage.warning('请选择作品分类')
    return
  }
  
  // 创建新作品
  const work = {
    id: Date.now(),
    title: newWork.value.title,
    description: newWork.value.description,
    category: newWork.value.category,
    status: 'draft',
    wordCount: 0,
    cover: '',
    createdAt: new Date().toISOString().split('T')[0],
    updatedAt: new Date().toISOString().split('T')[0]
  }
  
  works.value.unshift(work)
  
  // 重置表单
  newWork.value = {
    title: '',
    description: '',
    category: ''
  }
  
  showCreateDialog.value = false
  ElMessage.success('作品创建成功')
}

onMounted(() => {
  // 组件挂载后的逻辑
})
</script>

<style lang="scss" scoped>
.works {
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

  .works-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;

    .work-card {
      background: white;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
      transition: all 0.3s ease;
      cursor: pointer;

      &:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
      }

      .work-cover {
        position: relative;
        height: 180px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 48px;

        img {
          width: 100%;
          height: 100%;
          object-fit: cover;
        }

        .work-status {
          position: absolute;
          top: 12px;
          right: 12px;
          padding: 4px 8px;
          border-radius: 12px;
          font-size: 12px;
          font-weight: 500;
          color: white;

          &.draft {
            background: #909399;
          }

          &.writing {
            background: #e6a23c;
          }

          &.completed {
            background: #67c23a;
          }
        }
      }

      .work-info {
        padding: 20px;

        h3 {
          margin: 0 0 8px 0;
          font-size: 18px;
          font-weight: 600;
          color: #303133;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
        }

        .work-description {
          margin: 0 0 16px 0;
          color: #606266;
          font-size: 14px;
          line-height: 1.5;
          display: -webkit-box;
          -webkit-line-clamp: 2;
          -webkit-box-orient: vertical;
          overflow: hidden;
        }

        .work-meta {
          display: flex;
          justify-content: space-between;
          margin-bottom: 16px;

          .work-category {
            background: #f0f9ff;
            color: #0369a1;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 12px;
          }

          .work-words {
            color: #909399;
            font-size: 12px;
          }
        }

        .work-footer {
          display: flex;
          justify-content: space-between;
          align-items: center;

          .work-date {
            color: #909399;
            font-size: 12px;
          }

          .work-actions {
            display: flex;
            gap: 4px;
          }
        }
      }
    }
  }
}

@media (max-width: 768px) {
  .works {
    .page-header {
      flex-direction: column;
      align-items: flex-start;
      gap: 16px;
    }

    .filter-bar {
      flex-direction: column;
    }

    .works-grid {
      grid-template-columns: 1fr;
    }
  }
}
</style>