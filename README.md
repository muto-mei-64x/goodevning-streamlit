# コンテナ起動方法
VSCode開発環境上でコンテナ開発するため、
Docker Composeで定義されたコンテナ群をVSCodeタスクから起動するショートカットを作成している。
接続先環境とデバッグ要否によって使い分けること。

## 検証環境情報でコンテナを起動
検証アカウント上のインスタンスにデプロイするためのイメージ作成、
もしくはデバッグを使用しないローカル開発環境での動作確認に使用する。
環境変数は`Dockerfile.dev`を参照して起動する。

### VSCodeタスクを開く
[F1]キー押下しVScodeコマンドパレットを開く。
`Tasks: Run Task`を選択。
### 実行するタスクの選択
`Docker Up Dev`を選択し実行。
### コンテナ起動を確認
http://localhost:8083/
### アプリケーションコードを変更したときの反映方法
上記と同じ手順、Vscodeタスクでコンテナ起動する。

## 本番環境情報でコンテナを起動
本番アカウント上のインスタンスにデプロイするためのイメージ作成に使用する。
環境変数は`Dockerfile.prod`を参照して起動する。

### VSCodeタスクを開く
[F1]キー押下しVScodeコマンドパレットを開く。
`Tasks: Run Task`を選択。
### 実行するタスクの選択
`Docker Up Prod`を選択し実行
### コンテナ起動を確認
http://localhost:8083/
### アプリケーションコードを変更したときの反映方法
上記と同じ手順、Vscodeタスクでコンテナ起動する

## 検証環境情報でデバッグ可能なコンテナを起動
VSCodeデバッグ機能を使用したローカル開発環境での動作確認に使用する。
環境変数は`Dockerfile.devdebug`を参照して起動する。

### VSCodeタスクを開く
[F1]キー押下しVScodeコマンドパレットを開く。
`Tasks: Run Task`を選択。
### 実行するタスクの選択
`Docker Up Dev Debug`を選択し実行
処理が完了したらアプリケーションを起動する前にデバッガを起動する
### デバッガの起動
[ctrl]+[shift]+[D]で`実行とデバッグ`バーを開き、[F5]でデバッグを開始。
### コンテナ起動を確認
http://localhost:8083/
### アプリケーションコードを変更したときの反映方法
上記と同じ手順、Vscodeタスクでコンテナ起動する
