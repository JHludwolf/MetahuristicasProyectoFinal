Ter <- scan(file="Ins0.txt",sep="",what=integer(),nlines=10)

Est<-scan(file="Ins0.txt",sep="",what=integer(),skip=11,nlines=3)

Terminales<-matrix(Ter,nrow=10,ncol=4,byrow = TRUE)
Estaciones<-matrix(Est,nrow=3,ncol=4,byrow = TRUE)
puntosx=c()
puntosy=c()
puntosx2=c()
puntosy2=c()
for(i in 1:10){
  puntosx=c(puntosx,Terminales[i,3])
  puntosy=c(puntosy,Terminales[i,4])
}
for(i in 1:3){
  puntosx2=c(puntosx2,Estaciones[i,3])
  puntosy2=c(puntosy2,Estaciones[i,4])
}
plot(x=puntosx,y=puntosy,"p")
plot(x=puntosx2,y=puntosy2,"p")