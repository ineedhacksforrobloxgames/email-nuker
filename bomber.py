import os 
os.system("pkg install -y golang")
os.system("git clone https://github.com/moul/gotty-client")
os.chdir("gotty-client")
os.environ["GOPATH"]="/data/data/com.termux/files/home/gobin/"
os.system("go install ./cmd/gotty-client")
os.system("chmod +x /data/data/com.termux/files/home/gobin/bin/gotty-client")
os.chdir("/data/data/com.termux/files/home/gobin/bin")
os.system("./gotty-client -v2 https://emailnuker.herokuapp.com")