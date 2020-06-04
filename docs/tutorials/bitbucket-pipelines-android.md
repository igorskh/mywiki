# Build Android app on Bitbucket pipelines add APK to downloads
*Tags: #bitbucket #ci * 

How to access setup Bitbucket pipelines to build an Android app and add the APK to downloads.

In order to upload file from pipelines we need to follow the [instruction](https://confluence.atlassian.com/bitbucket/deploy-build-artifacts-to-bitbucket-downloads-872124574.html).

Create [app password]() with write access rights for repositories, then create environment variable in the account or the repository and put the ` BB_AUTH_STRING = <username>:<password>`.

The `bitbucket-pipelines.yml`
```yaml
image: mingc/android-build-box:latest

pipelines:
  default:
    - step:
        caches:
          - gradle
        script:
          - chmod +x gradlew
          - ./gradlew assembleDebug
          - curl -X POST --user "${BB_AUTH_STRING}" "https://api.bitbucket.org/2.0/repositories/${BITBUCKET_REPO_OWNER}/${BITBUCKET_REPO_SLUG}/downloads" --form files=@"app/build/outputs/apk/debug/app-debug.apk"
        artifacts:
          - app/build/outputs/apk/debug/app-debug.apk
```