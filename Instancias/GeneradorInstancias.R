
a<-sample(1:6,100,replace=TRUE)
x<-sample(0:100,100,replace=TRUE)
y<-sample(0:100,100,replace=TRUE)

b<-sample(10:15,32,replace=TRUE)
x1<-sample(0:100,32,replace=TRUE)
y1<-sample(0:100,32,replace=TRUE)

for (i in 1:100){
  
  cat(i,a[i],x[i],y[i],"\n")
}
cat("\n")
for (i in 1:32){
  cat(i,b[i],x1[i],y1[i],"\n")
}