#Pulsar plots code 
#Made by Juan G. Lebr√≥n Medina and Caryelis Bayona Figueroa
from pylab import plot,xlabel,ylabel,title,show,loadtxt,imshow,size,bone,ylim
from numpy import arange,concatenate
#Datas files must be in  same place has the code file  
print("Enter file name example: ao327_puppi_57865_Strip73.D164000+2223.0001_DM18.43_Z0_ACCEL_Cand_1")
print("Dont incluide the ending part like '.info' or '.pfd.profile' ")
TEST = input("Enter file name: ")
openfile = open((TEST + ".info"), "r")
#Getting values from the info file (Not sure how to make it easier)
for line in openfile.readlines():
    eq = line.find("=")
    if line.startswith(str("observation_time")):
        observation_time = line[eq + 2: -1]
    elif line.startswith(str("source_name")):
        source_name = line[eq + 3: -2]  # Without quote marks.
    elif line.startswith(str("dm")):
        dm = line[eq + 2: -1]
    elif line.startswith(str("p0")):
        p0 = line[eq + 2: -1]
    elif line.startswith(str("min_freq")):
        min_freq = line[eq + 2: -1]
    elif line.startswith(str("max_freq")):
        max_freq = line[eq + 2: -1]

#Profile file is just a column 
Profile = loadtxt(TEST+".pfd.profile")
"""
#Single pulse PULSAR PROFILE PLOT
M=size(Profile)
xpoints = arange(0,M)
plot(xpoints/M,Profile);title("Pulsar Profile")
xlabel("Phase");ylabel("Intensity");show()
"""
#TWO pulse PROFILE PLOT
TWOPULSE=[]
TWOPULSE.extend(Profile);TWOPULSE.extend(Profile)
D=size(TWOPULSE);doublexpoints = arange(0,D)
plot(2*doublexpoints/D,TWOPULSE);title("Two pulse Pulsar Profile "+ source_name)
xlabel("Phase");show()


#TvP file is an array ready to be plot it
TvP = loadtxt(TEST+".pfd.TvP")
TvP2 = concatenate((TvP,TvP),axis=1) #TWO time vs phase
imshow(TvP2,origin="lower",extent = [0 , 2, 0 , float(observation_time)],aspect=1/float(observation_time));#hot();
#gray()
bone();
title("Time vs Phase");xlabel("Phase");ylabel("Time (s)");show()


#FvP file is an array ready to be plot it 
FvP = loadtxt(TEST+".pfd.FvP")
FvP2 = concatenate((FvP,FvP),axis=1) #TWO Frequency vs Phase
imshow(FvP2,origin="lower",extent =[0,2,float(min_freq),float(max_freq)],aspect=1/(float(max_freq)-float(min_freq)));
title("Frequency vs Phase");xlabel("Phase");ylabel("Frequency (MHz)");show()


#DM file is an two column array  
DMcurve = loadtxt(TEST+".pfd.DMcurve")
#The second line on DMcurve are the chi (xá), it gets squared at the end
plot(DMcurve[:,0],DMcurve[:,1]**2);title("Dispersion Measure peak at "+dm+r" pc/cm$^3$")
xlabel(r"DM (pc/cm$^3$)");ylabel(r"Reduced $\chi^2$");ylim(0);show()    