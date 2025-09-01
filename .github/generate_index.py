# scripts/generate_index.py
import json
import os
from pathlib import Path
from collections import defaultdict

def get_images_by_directory(root_path):
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.svg')
    images_by_dir = defaultdict(list)
    
    for file_path in root_path.rglob('*'):
        if file_path.suffix.lower() in image_extensions and file_path.is_file():
            # 构建图片的相对路径，用于拼接URL
            relative_path = file_path.relative_to(root_path)
            # 获取目录名（相对于image目录）
            dir_name = relative_path.parent.name if relative_path.parent.name != '.' else 'root'
            
            # 获取不带扩展名的文件名
            name_without_ext = file_path.stem
            
            # 使用jsDelivr CDN链接
            url = f"https://cdn.jsdelivr.net/gh/HiFinTeam/risk-image@main/{relative_path.as_posix()}"
            
            images_by_dir[dir_name].append({
                "name": name_without_ext,
                "path": relative_path.as_posix(),
                "url": url
            })
    
    # 将defaultdict转换为普通dict，并按目录名排序
    result = {}
    for dir_name in sorted(images_by_dir.keys()):
        # 对每个目录内的图片按文件名排序
        images_by_dir[dir_name].sort(key=lambda x: x['name'])
        result[dir_name] = images_by_dir[dir_name]
    
    return result

if __name__ == "__main__":
    repo_root = Path('.')
    images_by_dir = get_images_by_directory(repo_root)
    
    # 生成JSON文件
    with open('images.json', 'w', encoding='utf-8') as f:
        json.dump(images_by_dir, f, indent=2, ensure_ascii=False)
    
    total_images = sum(len(images) for images in images_by_dir.values())
    print(f"Generated index for {total_images} images in {len(images_by_dir)} directories:")
    for dir_name, images in images_by_dir.items():
        print(f"  {dir_name}: {len(images)} images")
