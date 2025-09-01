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
   CREATE DATABASE writing_house CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   
   -- 创建用户（可选）
   CREATE USER 'writing_house'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON writing_house.* TO 'writing_house'@'localhost';
   ```

3. **后端配置**
   ```bash
   cd backend
   
   # 创建虚拟环境
   python -m venv venv
   
   # 激活虚拟环境
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   
   # 安装依赖
   pip install -r requirements.txt
   
   # 配置环境变量
   cp .env.example .env
   # 编辑 .env 文件，配置数据库连接等信息
   
   # 运行数据库迁移
   alembic upgrade head
   
   # 创建性能优化索引
   python database/create_indexes.py
   
   # 启动后端服务
   python main.py
   ```

4. **前端配置**
   ```bash
   cd frontend
   
   # 安装依赖
   npm install
   # 或使用 yarn
   yarn install
   
   # 启动开发服务器
   npm run dev
   # 或使用 yarn
   yarn dev
   ```

5. **访问应用**
   - 前端地址: http://localhost:5173
   - 后端API: http://localhost:8000
   - API文档: http://localhost:8000/docs

## 📁 项目结构

```
WritingHouse/
├── frontend/                 # 前端项目
│   ├── src/
│   │   ├── components/       # 公共组件
│   │   ├── views/           # 页面组件
│   │   ├── stores/          # 状态管理
│   │   ├── api/             # API接口
│   │   ├── router/          # 路由配置
│   │   ├── styles/          # 样式文件
│   │   └── utils/           # 工具函数
│   ├── package.json
│   └── vite.config.ts
├── backend/                  # 后端项目
│   ├── app/
│   │   ├── api/             # API路由
│   │   ├── core/            # 核心配置
│   │   ├── crud/            # 数据库操作
│   │   ├── db/              # 数据库配置
│   │   ├── models/          # 数据模型
│   │   ├── schemas/         # 数据验证
│   │   └── utils/           # 工具函数
│   ├── alembic/             # 数据库迁移
│   ├── database/            # 数据库脚本
│   ├── requirements.txt
│   └── main.py
└── README.md
```

## 🔧 配置说明

### 后端配置 (.env)

```env
# 数据库配置
MYSQL_SERVER=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=writing_house
MYSQL_PORT=3306

# JWT配置
SECRET_KEY=your-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# 文件上传配置
MAX_FILE_SIZE=10485760
UPLOAD_DIR=uploads
STATIC_DIR=static
```

### 前端配置

前端配置主要在 `vite.config.ts` 中，包括:
- 代理配置: API请求代理到后端
- 构建配置: 代码分割和优化
- 开发服务器配置

## 🚀 部署指南

### Docker 部署 (推荐)

1. **构建镜像**
   ```bash
   # 构建后端镜像
   docker build -t writinghouse-backend ./backend
   
   # 构建前端镜像
   docker build -t writinghouse-frontend ./frontend
   ```

2. **使用 Docker Compose**
   ```bash
   docker-compose up -d
   ```

### 传统部署

1. **后端部署**
   ```bash
   # 使用 gunicorn 部署
   pip install gunicorn
   gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
   ```

2. **前端部署**
   ```bash
   # 构建生产版本
   npm run build
   
   # 部署到 Nginx 或其他 Web 服务器
   cp -r dist/* /var/www/html/
   ```

## 🔍 性能优化

### 前端优化
- **本地缓存**: 5秒间隔的本地内容缓存
- **防抖机制**: 减少API调用频率
- **代码分割**: 按需加载减少初始包大小
- **组件懒加载**: 提升页面加载速度

### 后端优化
- **数据库索引**: 针对查询优化的索引设计
- **版本控制**: 自动清理旧版本，限制版本数量
- **字数统计链**: 优化统计更新逻辑
- **连接池**: 数据库连接池优化

## 🧪 测试

### 后端测试
```bash
cd backend
pytest tests/ -v
```

### 前端测试
```bash
cd frontend
npm run test
```

## 📝 开发指南

### 代码规范
- **前端**: ESLint + Prettier
- **后端**: Black + isort
- **提交**: 使用语义化提交信息

### 开发流程
1. Fork 项目
2. 创建功能分支
3. 编写代码和测试
4. 提交 Pull Request

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤:

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者和用户！

## 📞 联系我们

- 项目地址: [https://github.com/pointerStar007/WritingHouse](https://github.com/pointerStar007/WritingHouse)
- 问题反馈: [Issues](https://github.com/pointerStar007/WritingHouse/issues)
- 功能建议: [Discussions](https://github.com/pointerStar007/WritingHouse/discussions)

---

**WritingHouse** - 让创作更简单，让灵感不再流失 ✨