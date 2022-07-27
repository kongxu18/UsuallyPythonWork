import matplotlib.pyplot as plt
import scipy as sp

# make Data array to draw in
M = sp.zeros((500,500))

dpi = 300.0

# create a frameless mpl figure
fig, axes = plt.subplots(figsize=(M.shape[0]/dpi,M.shape[1]/dpi),dpi=dpi)
axes.axis('off')
fig.subplots_adjust(bottom=0,top=1,left=0,right=1)
axes.matshow(M,cmap='gray')


# set custom font
import matplotlib.font_manager as fm
ttf_fname = 'SimSun.ttf'
prop = fm.FontProperties(fname=ttf_fname)

# annotate something
axes.annotate('ABC',xy=(250,250),rotation=45,fontproperties=prop,color='white')
plt.show()
# get fig image data and read it back to numpy array
fig.canvas.draw()
w,h = fig.canvas.get_width_height()
Imvals = sp.fromstring(fig.canvas.tostring_rgb(),dtype='uint8')
ImArray = Imvals.reshape((w,h,3))