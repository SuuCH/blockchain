import hashlib
import json
import datetime

# blockchainのブロッククラス
class Block:
    # ブロックはインデックス、ハッシュ、タイムスタンプ、トランザクション、ナンス値を持つ
    def __init__(self, index, time, trans, p_hash):
        self.index = index
        self.time = time
        self.trans = trans
        self.p_hash = p_hash
         # 辞書化
        self.b_dict = {str(key):value for key, value in self.__dict__.items()}
        self.n_hash = self.calc_hash()
        
    def calc_hash(self):
        # 辞書型を文字列に変換
        b_string = json.dumps(self.b_dict, sort_keys=True).encode()
        return hashlib.sha256(b_string).hexdigest()

# blockChainのチェーンクラス
class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    # ジェネシスブロックの作成
    def create_genesis_block(self):
        return Block(0, 0, "GenesisBlock", "0")
    
    # 最後のブロックの取得
    def get_last_block(self):
        return self.chain[len(self.chain)-1]
    
    # ブロックの追加
    def add_block(self, new_block):
        new_block.p_hash = self.get_last_block().n_hash
        self.chain.append(new_block)
# 取引の登録（送り元、送り先、金額）
def reg_trans(sender, destination, money):
    trans = {
        "送り元": sender,
        "送り先": destination,
        "金額": money
    }
    return trans


myblockchain = BlockChain()
myblockchain.add_block(Block(1, str(datetime.datetime.now()),reg_trans("田中", "安倍", 100), myblockchain.chain[0].n_hash))
myblockchain.add_block(Block(2, str(datetime.datetime.now()),reg_trans("安倍", "佐藤", 200), myblockchain.chain[1].n_hash))

for i in range(0, len(myblockchain.chain)):
    print("Block : " , myblockchain.chain[i].index)
    print("Time : " , myblockchain.chain[i].time)
    print("Trans : " ,myblockchain.chain[i].trans)
    print("N_Hash : " , myblockchain.chain[i].n_hash)
    print("P_Hash : " , myblockchain.chain[i].p_hash)