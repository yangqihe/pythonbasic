import wx
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

scheduler_= BackgroundScheduler()
scheduler_.start()
jobId = "myjob"

def job_function():
    print("---job---")

def startBtnClick(evt):
    if(scheduler_.get_job(jobId)):
        print("---任务已经开始了，不要重复执行---")
    else:
        print("开始任务")
        scheduler_.add_job(job_function, 'interval', seconds=5, id=jobId)

def endBtnClick(evt):
    if(scheduler_.get_job(jobId)):
        scheduler_.remove_job(jobId)
        print("结束任务")
    else:
        print("任务已经停止")

app = wx.App()
win = wx.Frame(None,title='控制台',size=(200,275),pos=(1200,20))
panel = wx.Panel(win,size=(200,200))
panel.BackgroundColour = 'sky blue'

startBtn = wx.Button(win,label='开始任务',size=(100,10),pos=(0,200))
startBtn.BackgroundColour = 'red'
startBtn.Bind(wx.EVT_BUTTON,startBtnClick)

endBtn = wx.Button(win,label='停止任务',size=(100,10),pos=(100,200))
endBtn.Bind(wx.EVT_BUTTON,endBtnClick)

win.Show()
app.MainLoop()




