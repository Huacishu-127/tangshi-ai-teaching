git config --global user.name "你的名字"  
git config --global user.email "你的邮箱"  
ssh-keygen -t ed25519 -C "你的邮箱"  # 生成SSH密钥  
cat ~/.ssh/id_ed25519.pub  # 复制公钥到GitHub设置页
