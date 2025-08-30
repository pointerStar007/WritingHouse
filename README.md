# 写作小屋 (WritingHouse) V1.0

一个现代化的写作管理平台，帮助作者更好地组织和管理他们的创作内容。

## 🌟 项目简介

写作小屋是一个专为作者设计的全功能写作管理系统，提供了从创作灵感记录到作品发布的完整工作流程。系统采用现代化的Web技术栈，提供直观易用的用户界面和强大的功能支持。

## ✨ 主要功能

### 📊 仪表盘
- 写作统计概览
- 创作进度跟踪
- 写作目标管理
- 趋势分析图表

### 📝 作品管理
- 作品创建与编辑
- 章节管理
- 标签分类
- 状态跟踪（草稿、进行中、已完成）

### 💡 灵感管理
- 灵感记录与整理
- 分类标签
- 快速搜索
- 灵感转化为作品

### 👤 个人中心
- 个人资料管理
- 头像上传
- 社交媒体链接
- 个人统计

### ⚙️ 系统设置
- 个人信息设置
- 写作偏好配置
- 通知设置
- 隐私设置
- 系统主题切换

## 🛠️ 技术栈

### 前端
- **Vue 3** - 渐进式JavaScript框架
- **TypeScript** - 类型安全的JavaScript超集
- **Element Plus** - Vue 3组件库
- **Vite** - 现代化构建工具
- **Vue Router** - 官方路由管理器
- **Pinia** - 状态管理库

### 后端
- **FastAPI** - 现代化Python Web框架
- **SQLAlchemy** - Python SQL工具包和ORM
- **SQLite** - 轻量级数据库
- **Alembic** - 数据库迁移工具
- **Pydantic** - 数据验证库

### 开发工具
- **ESLint** - 代码质量检查
- **Prettier** - 代码格式化
- **TypeScript** - 类型检查

## 🚀 快速开始

### 环境要求

- Node.js >= 16.0.0
- Python >= 3.8
- npm 或 yarn

### 安装步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/yourusername/WritingHouse.git
   cd WritingHouse
   ```

2. **安装前端依赖**
   ```bash
   cd frontend
   npm install
   ```

3. **安装后端依赖**
   ```bash
   cd ../backend
   pip install -r requirements.txt
   ```

4. **数据库初始化**
   ```bash
   # 在backend目录下
   alembic upgrade head
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

## 📁 项目结构

```
WritingHouse/
├── frontend/                 # 前端项目
│   ├── src/
│   │   ├── api/             # API接口
│   │   ├── components/      # 公共组件
│   │   ├── layouts/         # 布局组件
│   │   ├── router/          # 路由配置
│   │   ├── stores/          # 状态管理
│   │   ├── styles/          # 样式文件
│   │   ├── types/           # TypeScript类型定义
│   │   ├── utils/           # 工具函数
│   │   └── views/           # 页面组件
│   ├── package.json
│   └── vite.config.ts
├── backend/                  # 后端项目
│   ├── app/
│   │   ├── api/             # API路由
│   │   ├── core/            # 核心配置
│   │   ├── crud/            # 数据库操作
│   │   ├── db/              # 数据库配置
│   │   ├── models/          # 数据模型
│   │   ├── schemas/         # Pydantic模式
│   │   ├── services/        # 业务逻辑
│   │   └── utils/           # 工具函数
│   ├── alembic/             # 数据库迁移
│   ├── main.py              # 应用入口
│   └── requirements.txt     # Python依赖
├── database/                 # 数据库相关文件
└── README.md                # 项目说明文档
```

## 🎨 界面预览

### 仪表盘
- 现代化的数据可视化界面
- 实时写作统计
- 直观的进度跟踪

### 作品管理
- 卡片式作品展示
- 便捷的筛选和搜索
- 拖拽式章节排序

### 设置页面
- 优雅的分组布局
- 响应式设计
- 玻璃拟态效果

## 🔧 配置说明

### 环境变量

**前端 (.env)**
```env
VITE_API_BASE_URL=http://localhost:8000
VITE_APP_TITLE=写作小屋
```

**后端**
- 数据库配置在 `app/core/config.py`
- 默认使用SQLite数据库

## 📝 开发指南

### 代码规范
- 前端使用ESLint + Prettier
- 后端遵循PEP 8规范
- 提交信息使用约定式提交格式

### 数据库迁移
```bash
# 创建新迁移
alembic revision --autogenerate -m "描述"

# 应用迁移
alembic upgrade head
```

### API文档
后端启动后，访问 `http://localhost:8000/docs` 查看自动生成的API文档。

## 🚀 部署指南

### 生产环境构建

1. **构建前端**
   ```bash
   cd frontend
   npm run build
   ```

2. **配置后端**
   - 修改数据库配置为生产环境
   - 设置安全密钥
   - 配置CORS策略

3. **部署选项**
   - **前端**: Vercel, Netlify, 或静态文件服务器
   - **后端**: Docker, 云服务器, 或Heroku

## 🤝 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

- 项目链接: [https://github.com/yourusername/WritingHouse](https://github.com/yourusername/WritingHouse)
- 问题反馈: [Issues](https://github.com/yourusername/WritingHouse/issues)

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者和用户！

---

**写作小屋 V1.0** - 让创作更简单，让灵感不再流失 ✨