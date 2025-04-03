# Git命令使用手册

## 一、git配置

#### 1.查看git是否配置全局的name/email

```shell
git config --list --global
```

#### 2.如果没有name/email添加

```shell
git config --global user.name "your-name"
git config --global user.email "your-emil@gmail.com"
```

#### 3.ssh生成密钥 

```shell
ssh-keygen -t rsa -b 4096 -C "your-emil@gmail.com"
```

- `-t rsa`：指定密钥类型为 RSA（推荐使用 RSA，因为它更通用）。

- `-b 4096`：指定密钥长度为 4096 位（更高的密钥长度意味着更高的安全性）。

- `-C "your-emil@gmail.com"`：添加一个注释，通常是你的电子邮件地址，用于标识密钥。

#### 4.生成两个文件公钥与私钥

- 私钥：保存在 ~/.ssh/id_rsa 文件中。

- 公钥：保存在 ~/.ssh/id_rsa.pub 文件中。

#### 5.将公钥添加到远程仓库

1. 复制公钥~/.ssh/id_rsa.pub 文件的内容。

2. 在远程Git服务的账户设置中（如GitHub的“Settings” -> “SSH and GPG keys” -> “New SSH key”），粘贴公钥内容，并保存。

   ![img](https://img2024.cnblogs.com/blog/2506499/202411/2506499-20241104230750104-2098843685.png)

#### 6.注意事项

- 确保你的`.ssh`目录和文件权限设置正确，通常目录权限为700（`chmod 700 ~/.ssh`），文件权限为600（`chmod 600 ~/.ssh/*）。

- 如果遇到连接问题，检查是否有防火墙或网络设置阻止了SSH连接。

  

## 二、git命令汇总

| 命令                                                         | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| **git init**                                                 | **创建本地仓库，暂存区**                                     |
| **git status**                                               | ***查看本地仓库、暂存区、合并冲突的命令十分重要***           |
| git init -b <分支名称>                                       | 创建本地仓库，暂存区和新建本地分支                           |
| **git branch**                                               | **查看本地分支**                                             |
| git branch -a                                                | 查看所有的本地分支和远程分支。                               |
| **git branch -vv**                                           | **查看所有分支最后提交的信息，常用**                         |
| git branch <分支名称>                                        | 已有仓库情况，新建分支，不切换到新分支                       |
| **git switch <分支名称>**                                    | **切换到分支**                                               |
| git checkout <分支名称>                                      | 切换到分支                                                   |
| **git checkout -b <分支名称>**                               | **已有仓库情况，新建分支，并切换到新分支**                   |
| git checkout <历史commit哈希> -- <文件名>                    | 恢复某个文件到某个提交的状态，如  git checkout abc123 -- file.txt |
| git checkout -t <远程仓库别名>/<远程分支>                    | 从远程仓库检出远程分支，并在本地创建一个新的跟踪分支。       |
| **git branch -m  <新分支名称>**                              | **将当前分支重命名为新分支名称**                             |
| git branch -m <原分支名称>  <新分支名称>                     | 重命名分支                                                   |
| **git branch -d <分支名称>**                                 | **删除分支（一般指是未合并的分支）**                         |
| **git branch -D <分支名称>**                                 | **强制删除分支（所有类型的分支）**                           |
| **git clone <远程项目地址>**                                 | **从远程仓库拉取到本地仓库的分支，无仓库权限**               |
| **git pull <远程仓库别名> (远程分支):(本地分支)<br />等效于git fetch + git merge** | **从远程仓库的远程分支拉取到本地仓库的本地分支；<br />本地分支可省略，代表拉取到当前分支；** |
| git pull -r <远程仓库别名> (远程分支)<br />等效于git fetch + git rebase | 将远程仓库的对应分支基变到本地仓库的分支。                   |
| git fetch <远程仓库别名> (远程分支)                          | 仅同步远程仓库的某个远程分支信息到本地仓库，不进行拉取实际文件 |
| **git fetch <远程仓库别名>**                                 | **同步远程仓库信息到本地仓库，不进行拉取实际文件**           |
| **git merge <被合并的分支名称>**                             | **合并分支**                                                 |
| git add .                # 添加解决后的文件<br/>git merge --continue     # 完成合并并生成提交 | 解决冲突并手动提交后，完成合并流程。                         |
| git merge --squash <被合并的分支名称><br/>git commit -m "合并<被合并的分支名称> 的改动" | 将目标分支的多个提交压缩成一个新提交。                       |
| **git push <远程仓库> (本地分支):(远程分支)**                | **从本地仓库的本地分支推送到远程仓库的远程分支；<br />远程分支和本地分支可省略，代表推送当前分支到远程相同名称的分支** |
| **git add <文件名1> <文件名2> <文件名3>**                    | **将某几个个文件从工作区转存到暂存区**                       |
| **git add .**                                                | **当前目录及子目录所有文件修改的文件从工作区转存到暂存区**   |
| **git commit -m "<备注内容>"**                               | **从暂存区提交到本地仓库**                                   |
| **git remote add <远程仓库别名> <远程仓库的url地址>**        | **从远程地址新建远程仓库别名**                               |
| **git remote -v**                                            | **查看远程仓库别名与远程地址绑定情况**                       |
| **git log**                                                  | **查看提交日志**                                             |
| git log --oneline                                            | 简洁输出提交日志，获取<commit号>                             |
| git log --graph --oneline                                    | 用图画的形式输出日志                                         |
| **git reset --soft <commit号>（常用）**                      | **本地仓库退回commit版本，暂存区和工作区内容不变**           |
| **git reset --mixed <commit号>（默认）**                     | **本地仓库和暂存区退回commit版本，工作区内容不变，一般用在想重新更新某个commit版本** |
| git reset --hard <commit号>（慎用）                          | 本地仓库、暂存区和工作区同时退回到commit版本，一般用在以确认退回某个commit版本，多人合作不允许使用这条命令，有可能会删除同伴的代码 |
| **git revert <commit号>（比git reset---hard安全更常用）**    | **相当于暂存区和工作区退回commit版本，已提交的历史本地仓库依然保留，多人合作请使用这条命令代替git reset** |
| **git --set-upstream <远程仓库别名>/<远程分支>**             | **用于设置本地分支跟踪远程分支。当你使用这个命令时，Git 会记住你指定的远程分支，这样在以后执行  git push 或  git pull 时，Git 就会自动知道应该与哪个远程分支交互。** |
| **git push --set-upstream <远程仓库别名> <本地分支>**        | **等同于git push + git --set-upstream，一般用在还没push过的新的远程仓库，可用在远程分支没有创建的情况** |
| **git push -u <远程仓库别名> <本地分支>**                    | **等同于git push --set-upstream <远程仓库别名> <本地分支>**  |
| **git branch --set-upstream-to=<远程仓库别名>/<远程分支> <本地分支>** | **用于设置本地分支跟踪远程分支。一般用在已经跟踪过，需要重新修改跟踪分支的命令。因此必须确保本地分支和远程分支都要存在，否则可以用上面前三条命令** |
| **git rebase <基变到的分支名称>**                            | **将当前的分支基变到对应的分支上，这里不太好理解，后面举例说明。** |
| git rebase <基变到的分支名称> <待基变分支>                   | git rebase main feature，意思是将feature分支的基础变更到main分支的头部，这样的效果相当于main分支往前多commit几次成了feature分支 |
| **git stash**                                                | **将工作区的状态（如：正在修改代码）进行保存，保存的名称系统定义** |
| git stash list                                               | 查看当前Git中已保存的所有名称，名称一般是stash@{0}           |
| git stash apply <已存储名称>                                 | 将存储名称里的内容读取到工作区，读取后不会删除存储名称       |
| git stash drop <已存储名称>                                  | 删除存储名称                                                 |
| **git stash pop**                                            | **将第一个stash堆栈中的第一个存储名称读取到工作区，并将这个存储名称从堆栈中删除** |
| git stash branch <新分支名称> <已存储名称>                   | 创建并切换到一个新分支来读取指定的存储名称，默认情况下读取stash堆栈中栈顶的存储 |
| **git stash show <已存储名称>**                              | **显示指定存储名称内存储的文件有哪些**                       |



## 三、重点学习演示

#### 1.git merge

git merge：合并分支，保留了原有分支的提交结构

![img](https://i-blog.csdnimg.cn/direct/39a98a7faa3b49a3819c7482caef2b27.png)

如图：

```shell
git switch master      		#切换到master分支（节点7）
git merge develop      		#在master分支合并develop分支（节点8）
git diff master develop      #查看分支差异，找到那里有冲突
#如果解决完冲突后
git add .
git commit -m '将某分支和某分支合并，解决冲突'
git push origin master
```



#### 2.git rebase

git rebase ：提交分支更加整洁（合并到master分支不要用，master分支合并到feature可以用）

![img](https://i-blog.csdnimg.cn/direct/2f72542e0a9d4e5db1685b6337f2215c.png)

```shell
git switch develop      		#切换到develop分支（节点6）
git rebase master      			#将master分支基变到develop分支（节点5',节点7'）图里的命令是错误的
git diff master develop      	#查看分支差异，找到那里有冲突
#如果解决完冲突后
git add .
git commit -m '将某分支基变到某分支，解决冲突'
git rebase --continue			#继续完成基变
```

备注：不同公司，不同情况有不同使用场景，不过大部分情况推荐如下：

单人开发的时候，拉公共分支最新代码的时候使用rebase，也就是`git pull -r`或`git pull –-rebase`。这样的好处很明显，提交记录会比较简洁。但有个缺点就是rebase以后我就不知道我的当前分支最早是从哪个分支拉出来的了，因为基底变了嘛，所以看个人需求了。

多人开发，往公共分支上合代码的时候，使用`merge`。如果使用rebase，那么其他开发人员想看主分支的历史，就不是原来的历史了，历史已经被你篡改了。举个例子解释下，比如张三和李四从共同的节点拉出来开发，张三先开发完提交了两次然后merge上去了，李四后来开发完如果rebase上去（注意李四需要切换到自己本地的主分支，假设先pull了张三的最新改动下来，然后执行<git rebase 李四的开发分支>，然后再git push到远端），则李四的新提交变成了张三的新提交的新基底，本来李四的提交是最新的，结果最新的提交显示反而是张三的，就乱套了。

正因如此，大部分公司其实会禁用rebase，不管是拉代码还是push代码统一都使用merge，虽然会多出无意义的一条提交记录“Merge … to …”，但至少能清楚地知道主线上谁合了的代码以及他们合代码的时间先后顺序。



#### 3.git stash

git stash：将工作区中已经保存的 和 暂存区的代码进行压栈保存；

![img](https://i-blog.csdnimg.cn/direct/d69e31cb07594f2f9a603269fe1367c3.png)

使用场景：

场景一：在分支 A 上正在工作，分支 B 上有个 bug 要处理；

```shell
git stash            #在分支 A 上执行该操作，将分支A上的修改代码进行保存
git checkout B       #切到分支 B，并处理 B 分支上的 bug
git checkout A       #切回到分支 A
git stash pop        #将 A 分支之前保存的修改代码进行恢复操作
```

场景二：冲突：代码开发完了准备提交，在 commit 之前，建议拉一下远端的代码；

```shell
git stash                 #将本地修改代码进行保存
git pull                  #拉取远端代码
git stash pop             #将保存的代码弹出
#本地处理可能出现的冲突,
git commit                #提交操作
git push
```



4.git cherry-pick

git cherry-pick：用于从一个分支中选择一个或多个提交（commit）并将其应用到当前分支。这在需要将特定的更改移植到另一个分支时非常有用，而不需要合并整个分支。

![img](https://i-blog.csdnimg.cn/direct/a6b32d935ef04294ae9bbb1d3ca99d3e.png)

如图

```shell
git checkout feature  #切换到feature分支
git log	--oneline	  #查看feature分支上各想要合并的commit哈希，如commit4、 commit6、 commit8
git checkout master   #切换回master分支
git cherry-pick commit4 commit6 commit8     #提交多个连续commit记录
```

解决冲突：如果在应用提交时出现冲突，Git 会提示你解决冲突。解决冲突后，使用以下命令标记冲突已解决并继续：

```shell
git add <resolved-files> 
git cherry-pick --continue
```

中止cherry-pick：如果决定不再继续 cherry-pick，可以使用以下命令中止操作：

```shell
git cherry-pick --abort
```

