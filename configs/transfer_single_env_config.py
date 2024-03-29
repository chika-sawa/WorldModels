import torch

TRANSFERED_SINGLE_ENV_CONFIG_DICT = {
    "experiment": {
        "env_list": [
            "AntBulletEnv-v0",
            "HopperBulletEnv-v0",
        ],
        "env_name": "HalfCheetahBulletEnv-v0",
        "train": {
            "model_lr": 6e-4,
            "value_lr": 8e-5,
            "action_lr": 8e-5,
            "eps": 1e-4,
            "seed_episodes": 10,  # 最初にランダム行動で探索するエピソード数
            "all_episodes": 50,  # 学習全体のエピソード数（300ほどで, ある程度収束します）
            "test_interval": 5,  # 何エピソードごとに探索ノイズなしのテストを行うか
            "model_save_interval": 20,  # NNの重みを何エピソードごとに保存するか
            "collect_interval": 100,  # 何回のNNの更新ごとに経験を集めるか（＝1エピソード経験を集めるごとに何回更新するか）
            "action_noise_var": 0.3,  # 探索ノイズの強さ
            "batch_size": 50,
            "chunk_length": 50,  # 1回の更新で用いる系列の長さ
            "imagination_horizon": 15,  # Actor-Criticの更新のために, Dreamerで何ステップ先までの想像上の軌道を生成するか
            "gamma": 0.9,  # 割引率
            "lambda_": 0.95,  # λ-returnのパラメータ
            "clip_grad_norm": 100,  # gradient clippingの値
            "free_nats": 3,  # KL誤差（RSSMのTransitionModelにおけるpriorとposteriorの間の誤差）がこの値以下の場合, 無視する
        },
        "transfer_type" : 'fractional',
        "transfer_path": "./logs/train_[AntBulletEnv-v0_HopperBulletEnv-v0]_test_[HalfCheetahBulletEnv-v0]_20230127-155422/episode_0040"
    },
    "model": {
        "state_dim": 30,  # 確率的状態の次元
        "rnn_hidden_dim": 200,  # 決定的状態（RNNの隠れ状態）の次元
    },
    "buffer" : {
        'buffer_capacity' : 200000
    },
    "logs": {"log_dir": "./logs"},
    "device": "cuda" if torch.cuda.is_available() else "cpu",
}
