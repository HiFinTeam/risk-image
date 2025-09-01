# Risk Image

这是一个用于管理风险相关图标的图片仓库，主要包含SVG格式的图标文件。

## 功能特性

- 🎨 提供统一的风险管理相关图标
- 📦 自动生成按目录分组的图片索引文件
- 🔄 GitHub Actions 自动更新
- 🌐 支持 jsDelivr CDN 访问
- 📝 简洁的图标名称（不包含文件扩展名）

## 项目结构

```
risk-image/
├── image/           # 图标文件目录
│   ├── product/     # 产品相关图标
│   └── dashboard/   # 仪表板相关图标
├── scripts/         # 脚本文件
├── workflows/       # GitHub Actions 配置
└── images.json      # 自动生成的图片索引（按目录分组）
```

## 使用方法

### 直接访问图标

通过 jsDelivr CDN 访问图标：

```
https://cdn.jsdelivr.net/gh/HiFinTeam/risk-image@main/image/product/icon-wrapper.svg
```

### 获取所有图标列表

访问 `images.json` 文件获取按目录分组的完整图标列表：

```json
{
  "product": [
    {
      "name": "icon-wrapper",
      "path": "image/product/icon-wrapper.svg",
      "url": "https://cdn.jsdelivr.net/gh/HiFinTeam/risk-image@main/image/product/icon-wrapper.svg"
    }
  ],
  "dashboard": [
    {
      "name": "test-icon",
      "path": "image/dashboard/test-icon.svg",
      "url": "https://cdn.jsdelivr.net/gh/HiFinTeam/risk-image@main/image/dashboard/test-icon.svg"
    }
  ]
}
```

### 在代码中使用

```javascript
// 获取所有产品图标
fetch('https://cdn.jsdelivr.net/gh/HiFinTeam/risk-image@main/images.json')
  .then(response => response.json())
  .then(data => {
    const productIcons = data.product;
    console.log('产品图标数量:', productIcons.length);
    
    // 使用图标名称（不包含扩展名）
    productIcons.forEach(icon => {
      console.log(`图标: ${icon.name}, URL: ${icon.url}`);
    });
  });
```

## 开发

### 添加新图标

1. 将SVG图标文件放入相应的目录（如 `image/product/`）
2. 推送到 main 分支
3. GitHub Actions 会自动更新 `images.json` 文件

### 创建新目录

1. 在 `image/` 目录下创建新的子目录（如 `image/charts/`）
2. 将相关图标放入该目录
3. 推送后会自动按目录分组

### 本地生成索引

```bash
python scripts/generate_index.py
```

## JSON 字段说明

- `name`: 图标名称（不包含文件扩展名）
- `path`: 文件在仓库中的相对路径
- `url`: 通过 jsDelivr CDN 访问的完整URL

## 支持的图片格式

- SVG (推荐)
- PNG
- JPG/JPEG
- GIF
- BMP
- WebP

## 许可证

本项目遵循相应的开源许可证。
