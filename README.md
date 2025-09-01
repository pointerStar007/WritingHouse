# 写作小屋 (WritingHouse) V2.0

一个现代化的网络小说创作平台，专为作者打造的全功能写作管理系统。

## 🌟 项目简介

写作小屋是一个专为网络小说创作者设计的B/S架构写作平台，提供从创作灵感记录到作品发布的完整工作流程。系统采用现代化的Web技术栈，提供沉浸式的写作体验和强大的功能支持。

## ✨ 核心功能

### 📊 写作统计
- **多维度统计**: 日/月/年三个周期的码字统计
- **实时数据**: 每日码字数、写作时长、创作效率分析
- **可视化图表**: 趋势分析和进度跟踪
- **写作目标**: 自定义目标设置和完成度监控

### 📝 智能编辑器
- **Markdown支持**: 类似Markdown的章节编辑器
- **实时预览**: 所见即所得的编辑体验
- **智能缓存**: 5秒本地缓存，30秒云端同步
- **版本管理**: 自动保存编辑历史，最多保存25个版本
- **自动滚动**: 智能光标跟随和滚动优化
- **字数统计**: 实时字数统计和进度显示

### 🏗️ 作品管理
- **层级结构**: 作品 → 卷 → 章节的完整管理体系
- **状态跟踪**: 草稿、连载中、已完结、暂停等状态管理
- **标签分类**: 灵活的标签系统和分类管理
- **批量操作**: 支持章节排序、批量编辑等操作

### 📖 预览与导出
- **阅读器预览**: 模拟真实阅读体验的预览模式
- **多格式导出**: 支持Word文档、PDF等多种格式导出
- **自定义样式**: 可配置的导出样式和格式

### 💡 灵感管理
- **快速记录**: 随时记录创作灵感和想法
- **智能分类**: 标签分类和快速搜索
- **灵感转化**: 一键将灵感转化为作品章节

### 👤 个人中心
- **个人资料**: 完整的作者信息管理
- **创作统计**: 个人创作数据和成就展示
- **偏好设置**: 个性化的写作环境配置

## 🛠️ 技术架构

### 前端技术栈
- **Vue 3** - 渐进式JavaScript框架
- **TypeScript** - 类型安全的JavaScript超集
- **Element Plus** - Vue 3 UI组件库
- **Vite** - 现代化构建工具
- **Vue Router** - 官方路由管理器
- **Pinia** - 轻量级状态管理
- **Monaco Editor** - 专业代码编辑器
- **ECharts** - 数据可视化图表库

### 后端技术栈
- **FastAPI** - 现代化Python Web框架
- **SQLAlchemy** - Python ORM框架
- **MySQL 8.0** - 关系型数据库
- **Alembic** - 数据库迁移工具
- **Pydantic** - 数据验证和序列化
- **JWT** - 用户认证和授权
- **python-docx** - 文档导出功能

### 性能优化
- **前端缓存**: 本地存储 + 云端同步的双层缓存机制
- **防抖机制**: 智能防抖减少不必要的API调用
- **版本控制**: 自动版本管理和清理机制
- **数据库优化**: 索引优化和查询性能提升

## 🚀 快速开始

### 环境要求

- **Node.js** >= 16.0.0
- **Python** >= 3.8
- **MySQL** >= 8.0
- **npm** 或 **yarn**

### 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/pointerStar007/WritingHouse.git
   cd WritingHouse
   ```

2. **数据库配置**
   ```sql
   -- 创建数据库
   CREATE DATABASE writinghouse CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   
   -- 创建用户（可选）
   CREATE USER 'writinghouse'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON writinghouse.* TO 'writinghouse'@'localhost';
   ```

3. **后端配置**
   ```bash
   cd backend
   
   # 安装依赖
   pip install -r requirements.txt
   
   # 配置数据库连接（修改 app/core/config.py）
   # DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/writinghouse"
   
   # 初始化数据库
   alembic upgrade head
   
   # 创建数据库索引（可选，提升性能）
   python database/create_indexes.py
   ```

4. **前端配置**
   ```bash
   cd ../frontend
   
   # 安装依赖
   npm install
   
   # 配置环境变量（.env.development）
   VITE_API_BASE_URL=http://localhost:8000
   VITE_APP_TITLE=写作小屋
   ```

### 运行项目

1. **启动后端服务**
   ```bash
   cd backend
   python main.py
   ```
   后端服务将在 `http://localhost:8000` 启动

2. **启动前端服务**
   ```bash
   cd frontend
   npm run dev
   ```
   前端服务将在 `http://localhost:5173` 启动

3. **访问应用**
   打开浏览器访问 `http://localhost:5173`

### 一键启动（Windows）

项目提供了便捷的启动脚本：

```bash
# PowerShell
.\start.ps1

# 批处理
start.bat

# GUI启动器
start_gui.bat
```

## 📁 项目结构

```
WritingHouse/
├── frontend/                 # 前端项目
│   ├── src/
│   │   ├── api/             # API接口封装
│   │   ├── components/      # 公共组件
│   │   │   ├── common/      # 通用组件
│   │   │   └── editor/      # 编辑器组件
│   │   ├── layouts/         # 布局组件
│   │   ├── router/          # 路由配置
│   │   ├── stores/          # Pinia状态管理
│   │   ├── styles/          # 全局样式
│   │   ├── types/           # TypeScript类型定义
│   │   ├── utils/           # 工具函数
│   │   │   └── editorCache.ts # 编辑器缓存管理
│   │   └── views/           # 页面组件
│   │       ├── dashboard/   # 仪表盘
│   │       ├── editor/      # 编辑器页面
│   │       ├── works/       # 作品管理
│   │       └── settings/    # 设置页面
│   └── package.json
├── backend/                  # 后端项目
│   ├── app/
│   │   ├── api/             # API路由
│   │   │   └── api_v1/      # API v1版本
│   │   ├── core/            # 核心配置
│   │   ├── crud/            # 数据库CRUD操作
│   │   ├── db/              # 数据库配置
│   │   ├── models/          # SQLAlchemy模型
│   │   ├── schemas/         # Pydantic模式
│   │   ├── services/        # 业务逻辑服务
│   │   └── utils/           # 工具函数
│   ├── alembic/             # 数据库迁移
│   ├── database/            # 数据库脚本
│   │   ├── create_indexes.py # 索引创建脚本
│   │   └── optimize_indexes.sql # 索引优化SQL
│   ├── main.py              # FastAPI应用入口
│   └── requirements.txt     # Python依赖
├── database/                 # 数据库设计文档
├── launcher_*.py            # GUI启动器
├── start.*                  # 启动脚本
└── README.md                # 项目文档
```

## 🎨 功能特色

### 智能编辑体验
- **双层缓存机制**: 本地5秒缓存 + 云端30秒同步，确保数据安全
- **无感知保存**: 编辑过程中自动保存，不打断创作思路
- **版本历史**: 自动记录编辑历史，支持版本回滚
- **智能滚动**: 光标自动跟随，优化长文档编辑体验

### 数据安全保障
- **多重备份**: 本地缓存 + 数据库存储 + 版本历史
- **自动恢复**: 意外关闭后自动恢复未保存内容
- **版本管理**: 最多保存25个历史版本，自动清理旧版本

### 性能优化
- **防抖机制**: 智能防抖减少服务器压力
- **数据库索引**: 优化查询性能，提升响应速度
- **前端缓存**: 减少网络请求，提升用户体验

## 🔧 配置说明

### 环境变量

**前端配置 (.env.development)**
```env
VITE_API_BASE_URL=http://localhost:8000
VITE_APP_TITLE=写作小屋
```

**后端配置 (app/core/config.py)**
```python
# 数据库配置
DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/writinghouse"

# JWT配置
SECRET_KEY = "your-secret-key"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 文件上传配置
UPLOAD_DIR = "./uploads"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
```

### 编辑器配置

```typescript
// 缓存配置
const cacheConfig = {
  maxVersions: 25,        // 最大缓存版本数
  cacheInterval: 5000,    // 本地缓存间隔（5秒）
  syncInterval: 30000     // 云端同步间隔（30秒）
}

// 自动保存配置
const autoSaveConfig = {
  debounceDelay: 2000,    // 防抖延迟（2秒）
  enabled: true           // 是否启用自动保存
}
```

## 📝 开发指南

### 代码规范
- **前端**: ESLint + Prettier + TypeScript
- **后端**: PEP 8 + Black + isort
- **提交**: 约定式提交格式

### 数据库操作

```bash
# 创建新迁移
alembic revision --autogenerate -m "添加新功能"

# 应用迁移
alembic upgrade head

# 回滚迁移
alembic downgrade -1

# 查看迁移历史
alembic history
```

### API文档

启动后端服务后，访问以下地址查看API文档：
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🚀 部署指南

### 生产环境构建

1. **前端构建**
   ```bash
   cd frontend
   npm run build
   ```

2. **后端配置**
   ```python
   # 生产环境配置
   DEBUG = False
   DATABASE_URL = "mysql+pymysql://user:password@host:port/database"
   SECRET_KEY = "production-secret-key"
   ```

3. **Docker部署**
   ```dockerfile
   # 前端Dockerfile
   FROM nginx:alpine
   COPY dist/ /usr/share/nginx/html/
   
   # 后端Dockerfile
   FROM python:3.9-slim
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

### 部署选项

- **前端**: Vercel, Netlify, 阿里云OSS, 腾讯云COS
- **后端**: 阿里云ECS, 腾讯云CVM, Docker, Kubernetes
- **数据库**: 阿里云RDS, 腾讯云CDB, 自建MySQL

## 🔄 更新日志

### V2.0 (2024-01)
- ✨ 新增智能缓存机制，提升编辑体验
- ✨ 优化自动保存逻辑，减少编辑中断
- ✨ 改进编辑器滚动功能，增强长文档编辑
- ✨ 添加版本管理系统，支持历史回滚
- 🐛 修复自动保存时编辑器刷新问题
- 🐛 修复滚动条自动下滚功能失效
- ⚡ 优化数据库查询性能，添加必要索引
- ⚡ 优化字数统计更新链，减少重复计算

### V1.0 (2024-01)
- 🎉 项目初始版本发布
- ✨ 完整的作品管理功能
- ✨ Markdown编辑器支持
- ✨ 写作统计和数据可视化
- ✨ 用户认证和权限管理

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 贡献方式

1. **报告问题**: 在 [Issues](https://github.com/pointerStar007/WritingHouse/issues) 中报告bug或提出建议
2. **功能请求**: 提出新功能需求和改进建议
3. **代码贡献**: 提交Pull Request
4. **文档改进**: 完善项目文档和使用说明

### 开发流程

1. Fork 项目到你的GitHub账户
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

### 代码审查

- 确保代码符合项目规范
- 添加必要的测试用例
- 更新相关文档
- 通过所有CI检查

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

- **项目主页**: [https://github.com/pointerStar007/WritingHouse](https://github.com/pointerStar007/WritingHouse)
- **问题反馈**: [Issues](https://github.com/pointerStar007/WritingHouse/issues)
- **功能建议**: [Discussions](https://github.com/pointerStar007/WritingHouse/discussions)

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者和用户！特别感谢以下开源项目：

- [Vue.js](https://vuejs.org/) - 渐进式JavaScript框架
- [FastAPI](https://fastapi.tiangolo.com/) - 现代化Python Web框架
- [Element Plus](https://element-plus.org/) - Vue 3组件库
- [Monaco Editor](https://microsoft.github.io/monaco-editor/) - 代码编辑器
- [ECharts](https://echarts.apache.org/) - 数据可视化库

---

**写作小屋 V2.0** - 让创作更流畅，让灵感不再流失 ✨

> 专为网络小说创作者打造的现代化写作平台，提供沉浸式的创作体验和强大的管理功能。