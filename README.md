# robot-controller-client-browser
Webブラウザを用いてSota(CommU or Puppet)内のRobotControllerと通信し、操作するサンプルプログラムです。

このプログラムを実行する際は、Sotaの中で[RobotControllerを起動](https://github.com/social-robotics-lab/RobotController_bin)しておいてください。

## Install
```
git clone https://github.com/social-robotics-lab/robot-controller-client-browser.git
```

## Docker build and run
```
cd robot-controller-client-browser
docker compose build
docker compose run --rm --service-ports app
```

上記を実行後、http://127.0.0.1:5000にアクセスしてください。