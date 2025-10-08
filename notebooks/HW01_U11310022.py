from obspy import UTCDateTime, read
from obspy.clients.fdsn import Client

import matplotlib.pyplot as plt

# 設定參數
client = Client("IRIS")
starttime = UTCDateTime("2025-10-07T23:52:12")
endtime = starttime + 120  # 持續 120 秒

# 抓取地震波 (使用示例台站: IU.ANMO.00.BHZ)
st = client.get_waveforms(network="IU", station="ANMO", location="00", channel="BHZ",
                         starttime=starttime, endtime=endtime)

# 畫圖
fig = plt.figure(figsize=(10, 4))
st.plot(outfile="/workspaces/geophysics-class-2025/notebooks/HW01_U11310022_waveform.png", fig=fig)
plt.close(fig)
