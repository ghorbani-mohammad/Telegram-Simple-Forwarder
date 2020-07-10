#!/usr/bin/env bash
echo y | keytool -genkeypair -deststoretype pkcs12 -dname "cn=Pourya MandiSanam, ou=beshkaf.tika-team.ir, o=tika-team, c=98" -alias bot -keypass A8UeX156jDlJNHZkcTp -keystore android_signkey.jks -storepass A8UeX156jDlJNHZkcTp -validity 10000 -keysize 1024
