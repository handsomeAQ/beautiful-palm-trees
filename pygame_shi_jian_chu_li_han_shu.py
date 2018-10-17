#处理事件：
#pygame.event.get()
#从事件队列中获得事件列表，即获得所有被队列的事件
#for event. in pygame.event.get():
    #if event.type == pygame.QUIT:
        #sys.exit()

#pygame.event.poll()
#从事件队列中获取一个事件
#pygame.event.clear()

#操作事件队列：
#pygame.event.set_blocked()
#pygame.event.get_blocked()
#pygame.event.set_allowed()

#生成事件：
#pygame.event.post()
#pygame.event.Event()