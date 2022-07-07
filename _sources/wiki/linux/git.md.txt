---
layout: page
date: 20220412000000
title:
categories:
tags: 
udc: 
reference:

1|https://www.v2ex.com/t/848517#reply35

 
---

## git

### Init

```bash
# 以 Github 为例
# 从网页登入 Github 账号
# 进入 https://github.com/new
# 创建新仓库

echo "# yyy" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/xxx/yyy.git
git push -u origin main
```

## Other

```bash
git reset --hard HEAD^
    # 回退到上个版本


git branch -a
    # 查看所有分支


git checkout -b test
    # 创建并切换分支到 test


git checkout new
    # 切换到分支 new


git branch -d test
    # 删除分支 test


git branch -D test
    # 强制删除分支 test


git push origin test:test
    # 上传本地分支 test 到远程分支 test


git push origin :test
    # 只删除远程分支 test (分支名前的冒号代表删除)


git pull origin test
    # 同步本地分支和远程分支 test


git remote -v
    # 查看所有远程库的远程地址


git remote add upstream <URL>
    # 添加源分支 URL


git fetch upstream
    # 从源分支获取最新的代码



# Merge between two local
# 合并两个本地分支 repositories {
git init new

git clone repo1.git
git clone repo2.git

git remote add repo1 ../repo1

git fetch repo1

git merge repo1/master
git merge repo2/master



fd -t f -x bash -c 'touch -d "$(git log -1 --format='%ai' $1)" $1' bash {}
    # 还原文件的修改日期
    # 需要使用 git clone xxx.git 命令 完整克隆分支


# }




git push origin --delete test
    # 删除


git branch -d -r origin/master
    # 中断
```


## CheatSheet

https://github.com/LeCoupa/awesome-cheatsheets/blob/master/tools/git.sh


## config


## Command

### clone

```bash
git clone --reference https://
```

### archive

```bash
git archive --format=tar main | zstd > main.zst

git archive -o main.tar main
    # Note that the output format is inferred by the extension of the output file.

git archive -o main.zst main
```

### worktree

```bash
git worktree add ../test-dir
    # Create new

git worktree remove test-dir
    # Delete a dir

git worktree add test-dir main
    # Copy a dir into main
```

### 冲突


```bash
# 先把当前没做完的活 stash 了, 然后 pull , pull 完, 你同事的 commit 就合并进去了, 这个时候, 在把 stash 的内容取出来。
git stash
git pull --rebase
git stash pop

```
### Info

```bash
git fetch # 将本地分支与远程保持同步
git fetch -p 获取远程仓库的新分支以及删除远程仓库已删除的分支

```

#### remote


```bash
git remote -v
    # 查看远程仓库地址

```

### branch

```bash
git branch -r 
    # 查看所有远程分支

git branch -a 
    # 查看本地和远程所有的分支

```

### Merge

#### merge

#### rebase

[1|https://chenshinan.github.io/2021/12/09/%E5%BF%AB%E6%8D%B7%E8%AE%B0%E5%BF%86/#more]
```bash
git rebase
把一个分支中的修改整合到另一个分支的办法有两种： merge 和 rebase 。 rebase 可以把在一个分支里提交的改变移到另一个分支里重放一遍。
rebase 的操作不当，可能导致原分支被修改等后果。作为一个危险操作，需要慎重。
变基操作解决冲突后应执行 git add . 和 git rebase --continue ，而不是 git commit 命令
A分支切出来一个B分支，当前在B分支，已经做了两个提交，切回A分支也做了两个提交，再切回B分支
# B分支合并A分支的提交记录
git rebase A
# 处理完冲突继续合并
git add .
git rebase –continue
# 跳过
git rebase –skip
# 取消合并
git rebase –abort
# 最后再切回A分支，A merge B，这样A中的提交记录就是整洁的了（没有merge记录）

```


###

git缓存区
git stash save xxx 保存stash有名字
git stash clear 清空缓存
git stash list 缓存列表
git stash apply stash@{0} 应用缓存

git rm -r --cached . 
    # 删除本地缓存

### Version


版本回退

git log
git reset --hard HEAD^ //删除工作空间改动代码，撤销commit，撤销git add
git reset --soft HEAD^ //撤回commit，代码仍然在add中
git reset --mixed HEAD^ //不删除工作空间改动代码，撤销commit，并且撤销git add


### Branch

#### Rename


分支强行替换名字

git branch -m master old-master
git branch -m develop master
git push -f origin master


### Tag

#### tag

```bash
git branch <new-branch-name> <tag-name>
删除tag
1
2
git tag -d [tag];
git push origin :[tag]
```