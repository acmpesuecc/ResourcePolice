import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Resouce Police")
n = Notify.Notification.new("ResourcePolice","<b>CPU Usage high!</b>","dialog-information")
n.set_urgency(1)

n.show()

