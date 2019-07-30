from colorama import Fore,Style
from getpass import getpass #遮挡密码
from service.user_service import UserService
from service.news_service import NewsService
from service.role_service import RoleService
from service.type_service import TypeService
import os #清理控制台之前的内容
import sys
import time

__user_service=UserService()
__news_service=NewsService()
__role_service=RoleService()
__type_service=TypeService()

while True:
    os.system("cls")
    print(Fore.LIGHTBLUE_EX, "\n\t===========")#\n另起一行 \t=Tab=4个空格
    print(Fore.LIGHTBLUE_EX, "\n\t欢迎使用新闻管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t============")
    print(Fore.LIGHTGREEN_EX, "\n\t1.登录系统")
    print(Fore.LIGHTGREEN_EX, "\n\t2.退出系统")
    print(Style.RESET_ALL)
    opt=input("\n\t输入操作编号:")
    if opt=="1":
        username=input("\n\t用户名:")
        password=getpass("\n\t密码:")
        result=__user_service.login(username,password)
        #登录成功
        if result==True:
            #查询角色
            role = __user_service.search_user_role(username)

            while True:
                os.system("cls")
                if role=="新闻编辑":
                    print(Fore.LIGHTGREEN_EX, "\n\t1.发表新闻")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.编辑新闻")
                    print(Fore.LIGHTRED_EX, "\n\tback.退出登录")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号")
                    if opt=="1":
                        os.system("cls")
                        title=input("\n\t新闻标题:")
                        userid=__user_service.search_user_id(username)
                        result=__type_service.search_list()

                        for index in range(len(result)):
                            one = result[index]
                            print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, one[1]))
                        print(Style.RESET_ALL)
                        opt = input("\n\t类型编号:")
                        type_id = result[int(opt) - 1][0]
                        #新闻正文内容
                        contnet_id=100
                        is_top=input("置顶级别(0-5):")
                        is_commit=input("\n\t是否提交(Y/N):")
                        if is_commit=="Y" or is_commit=="y":
                            __news_service.insert(title,userid,type_id,contnet_id,is_top)
                            print("\n\t保存成功(3秒自动返回)")
                            time.sleep(3)


                elif role=="管理员":
                    print(Fore.LIGHTGREEN_EX,"\n\t1.新闻管理")
                    print(Fore.LIGHTGREEN_EX,"\n\t2.用户管理")
                    print(Fore.LIGHTRED_EX,"\n\tback.退出登录")
                    print(Fore.LIGHTRED_EX,"\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt=input("\n\t输入操作编号")
                    if opt=="1":
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.审批新闻")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.删除新闻")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号")
                            if opt=="1":
                                page=1
                                while True:
                                    os.system("cls")
                                    count_page=__news_service.search_unreview_count_page()
                                    result=__news_service.search_unreview_list(page)
                                    for index in range(len(result)):
                                        one=result[index]
                                        print(Fore.LIGHTGREEN_EX, "\n\t%d\t%s\t%s\t%s"%(index+1,one[1],one[2],one[3]))
                                    print(Fore.LIGHTGREEN_EX, "\n\t------------")
                                    print(Fore.LIGHTGREEN_EX, "\n\t%d/%d"%(page,count_page))
                                    print(Fore.LIGHTGREEN_EX, "\n\t------------")
                                    print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTGREEN_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTGREEN_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号")
                                    if opt=="back":
                                        break
                                    elif opt=="prev" and page>1:
                                        page-=1
                                    elif opt=="next" and page<count_page:
                                        page+=1
                                    elif int(opt)>=1 and int(opt)<=10:
                                        news_id=result[int(opt)-1][0]
                                        __news_service.update_unreview_news(news_id)
                                        result=__news_service.search_cache(news_id)
                                        title=result[0]
                                        username=result[1]
                                        type=result[2]
                                        content_id=result[3]
                                        content="100"
                                        is_top=result[4]
                                        create_time=str(result[5])#redis没有日期类型，需要转化成字符串
                                        __news_service.cache_news(news_id,title,username,type,content_id,is_top,create_time)
                            elif opt=="2":
                                page=1
                                while True:
                                    os.system("cls")
                                    count_page=__news_service.search_count_page()
                                    result=__news_service.search_list(page)
                                    for index in range(len(result)):
                                        one=result[index]
                                        print(Fore.LIGHTGREEN_EX, "\n\t%d\t%s\t%s\t%s"%(index+1,one[1],one[2],one[3]))
                                    print(Fore.LIGHTGREEN_EX, "\n\t------------")
                                    print(Fore.LIGHTGREEN_EX, "\n\t%d/%d"%(page,count_page))
                                    print(Fore.LIGHTGREEN_EX, "\n\t------------")
                                    print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTGREEN_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTGREEN_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号")
                                    if opt=="back":
                                        break
                                    elif opt=="prev" and page>1:
                                        page-=1
                                    elif opt=="next" and page<count_page:
                                        page+=1
                                    elif int(opt)>=1 and int(opt)<=10:
                                        news_id=result[int(opt)-1][0]
                                        __news_service.delete_by_id(news_id)
                            elif opt=="back":
                                break

                    elif opt=="2":
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.添加用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.修改用户")
                            print(Fore.LIGHTGREEN_EX, "\n\t3.删除用户")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号")
                            if opt=="back":
                                break
                            elif opt=="1":
                                os.system("cls")
                                username=input("\n\t用户名:")
                                password=getpass("\n\t密码:")
                                repassword=getpass("\n\t重复密码:")
                                if password!=repassword:
                                    print("\n\t两次密码不一致(3秒自动返回)")
                                    time.sleep(3)
                                    continue
                                email=input("\n\t邮箱:")
                                result=__role_service.search_list()
                                for index in range(len(result)):
                                    one=result[index]
                                    print(Fore.LIGHTBLUE_EX,"\n\t%d.%s"%(index+1,one[1]))
                                print(Style.RESET_ALL)
                                opt=input("\n\t角色编号:")
                                role_id=result[int(opt)-1][0]
                                __user_service.insert(username,password,email,role_id)
                                print("\n\t保存成功(3秒自动返回)")
                                time.sleep(3)
                            elif opt=="2":
                                page = 1
                                while True:
                                    os.system("cls")
                                    count_page = __user_service.search_count_page()
                                    result = __user_service.search_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTGREEN_EX,
                                              "\n\t%d\t%s\t%s" % (index + 1, one[1], one[2]))
                                    print(Fore.LIGHTGREEN_EX, "\n\t------------")
                                    print(Fore.LIGHTGREEN_EX, "\n\t%d/%d" % (page, count_page))
                                    print(Fore.LIGHTGREEN_EX, "\n\t------------")
                                    print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTGREEN_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTGREEN_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif int(opt) >= 1 and int(opt) <= 10: #修改用户
                                        os.system("cls")
                                        user_id=result[int(opt)-1][0]
                                        username = input("\n\t新用户名:")
                                        password = getpass("\n\t新密码:")
                                        repassword = getpass("\n\t重复新密码:")
                                        if password != repassword:
                                            print("\n\t两次密码不一致(3秒自动返回)")
                                            time.sleep(3)
                                            continue
                                        email = input("\n\t新邮箱:")

                                        result = __role_service.search_list()
                                        for index in range(len(result)):
                                            one = result[index]
                                            print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, one[1]))
                                        print(Style.RESET_ALL)
                                        opt = input("\n\t角色编号:")
                                        role_id = result[int(opt) - 1][0]
                                        opt=input("\n\t是否保存(Y/N)")
                                        if opt=="Y" or opt=="y":
                                            __user_service.update(user_id,username,password,email,role_id)
                                            print("\n\t保存成功(3秒自动返回)")
                                            time.sleep(3)
                            elif opt=="3":
                                page = 1
                                while True:
                                    os.system("cls")
                                    count_page = __user_service.search_count_page()
                                    result = __user_service.search_list(page)
                                    for index in range(len(result)):
                                        one = result[index]
                                        print(Fore.LIGHTGREEN_EX,
                                              "\n\t%d\t%s\t%s" % (index + 1, one[1], one[2]))
                                    print(Fore.LIGHTGREEN_EX, "\n\t------------")
                                    print(Fore.LIGHTGREEN_EX, "\n\t%d/%d" % (page, count_page))
                                    print(Fore.LIGHTGREEN_EX, "\n\t------------")
                                    print(Fore.LIGHTGREEN_EX, "\n\tback.返回上一层")
                                    print(Fore.LIGHTGREEN_EX, "\n\tprev.上一页")
                                    print(Fore.LIGHTGREEN_EX, "\n\tnext.下一页")
                                    print(Style.RESET_ALL)
                                    opt = input("\n\t输入操作编号")
                                    if opt == "back":
                                        break
                                    elif opt == "prev" and page > 1:
                                        page -= 1
                                    elif opt == "next" and page < count_page:
                                        page += 1
                                    elif int(opt) >= 1 and int(opt) <= 10: #修改用户
                                        os.system("cls")
                                        user_id = result[int(opt) - 1][0]
                                        __user_service.delete_by_id(user_id)
                                        print("\n\t删除成功(3秒自动返回)")
                                        time.sleep(3)






                    elif opt=="back":
                        break
                    elif opt=="exit":
                        sys.exit(0)
        else:
            print("\n\t登录失败(3秒自动返回)")
            time.sleep(3)
    elif opt=="2":
        # break
        sys.exit(0)#安全退出
