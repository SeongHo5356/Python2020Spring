class RemoteControl:
    enabledChannelList = []
    channel_list2=[]
    current_channel = ''
    blocked_channel =[]
    
    def powerOnRemoteControl(self, channel_list):#채널의 길이 return
        self.enabledChannelList = channel_list[:]
        self.channel_list2 = self.enabledChannelList[:]
        #현재 시정충인 채절 맨앞쪽에 배치
        return(len(self.enabledChannelList))

    
    def gotoChannel(self, channel):#직접이동할 채널 입력받고, 채널 이름 return
        for i in range(0, len(self.channel_list2)):
            if (str(channel) == self.channel_list2[i][0]):
                temp = self.channel_list2[i]
                del(self.channel_list2[i])
                self.channel_list2.insert(0,temp)
                self.current_channel = self.channel_list2[0][0]
                return self.channel_list2[0][1]         
            else:
                return 
    
    
    def nextChannel(self):#현재 채널다음목록으로 넘기고 return 채널이름
        for i in range(0, len(self.enabledChannelList)):
            if (self.enabledChannelList[i][0]==self.current_channel):
                if (i==len(self.enabledChannelList)-1):
                    temp = self.enabledChannelList[0][0]
                else:
                    temp = self.enabledChannelList[i+1][0]
                
                for k in range(0, len(self.channel_list2)):
                    if (temp == self.channel_list2[k][0]):
                        new_temp = self.channel_list2[k]
                        del(self.channel_list2[k])
                        self.channel_list2.insert(0,new_temp)
                        self.current_channel = self.channel_list2[0][0]
                        return self.channel_list2[0][1]
                

    def previousChannel(self):
        for i in range(0, len(self.enabledChannelList)):
            if (self.enabledChannelList[i][0]==self.current_channel):
                temp = self.enabledChannelList[i-1][0]
                for k in range(0, len(self.channel_list2)):
                    if (temp == self.channel_list2[k][0]):
                        new_temp = self.channel_list2[k]
                        del(self.channel_list2[k])
                        self.channel_list2.insert(0,new_temp)
                        self.current_channel = self.channel_list2[0][0]
                        return self.channel_list2[0][1]    

    def blockChannel(self):
        blocked_item = self.channel_list2[0]
        self.blocked_channel.append(blocked_item)
        del(self.channel_list2[0])
        for i in range(0, len(self.enabledChannelList)-1):
            if(self.enabledChannelList[i]==blocked_item):
                del(self.enabledChannelList[i])
        self.current_channel = self.channel_list2[0][0]

        return self.channel_list2[0][1]


    def unblockChannel(self, restore_item):
        for i in range(0, len(self.blocked_channel)):
            if (str(restore_item) ==self.blocked_channel[i][0]):
                self.enabledChannelList.append(self.blocked_channel[i])
                self.channel_list2.append(self.blocked_channel[i])
                self.enabledChannelList.sort()
                self.current_channel = self.channel_list2[0][0]
                return 1
            else:
                return -1

      
    def powerOffRemoteControl(self):
        with open('ouput.csv','w') as file:
            for i in range(0, len(self.enabledChannelList)):
                file.write(self.enabledChannelList[i][0])
                file.write(",")
                file.write(self.enabledChannelList[i][1]) 
                file.write(" ")
                file.write('\n')


