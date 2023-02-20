# UR_23Spring

Launch UR Simulator as a docker container:

`$ sudo docker run --rm -dit -e ROBOT_MODEL=UR3 -p 5900:5900 -p 6080:6080 -p 29999:29999 -p 30001-30004:30001-30004 universalrobots/ursim_e-series`

http://<localaddress>:6080/vnc.html
