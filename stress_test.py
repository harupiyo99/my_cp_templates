import os
import subprocess
import random

# ==================== 設定 ====================
PROBLEM = "A"          # 問題のアルファベット (例: "A", "B", "C", "D" など)
NUM_TESTS = 100        # 生成するテストケースの数
# ==============================================

# ディレクトリ名
DIR_INPUT = f"input_{PROBLEM}"
DIR_OUTPUT = f"output_{PROBLEM}"
DIR_OUTPUT_STUPID = f"output_stupid_{PROBLEM}"

def setup_directories():
    """必要なディレクトリを作成する"""
    for d in [DIR_INPUT, DIR_OUTPUT, DIR_OUTPUT_STUPID]:
        os.makedirs(d, exist_ok=True)

def compile_cpp():
    """C++のプログラムをコンパイルする"""
    print("Compiling C++ files...")
    
    # 本命解のコンパイル
    res_main = subprocess.run(["g++", "-O3", f"{PROBLEM}.cpp", "-o", f"{PROBLEM}_exe"])
    if res_main.returncode != 0:
        print(f"Error: Failed to compile {PROBLEM}.cpp")
        exit(1)
        
    # 愚直解のコンパイル
    res_stupid = subprocess.run(["g++", "-O3", f"{PROBLEM}_stupid.cpp", "-o", f"{PROBLEM}_stupid_exe"])
    if res_stupid.returncode != 0:
        print(f"Error: Failed to compile {PROBLEM}_stupid.cpp")
        exit(1)
        
    print("Compilation successful!\n")

def generate_input():
    """
    【ここを問題ごとに書き換えてください】
    ランダムな入力データを生成し、文字列input_strとして返す関数
    """

    # 下のは消しても構わない
    input_str = ""

    # 例: 
    # 1. [l, r]の中からランダムで整数変数Nを生成
    # N = random.randint(l, r)

    # 2. a~zの中からランダムで文字変数生成
    # c = random.choice(string.ascii_lowercase)

    # 3. 文字列変数 (例: 長さ [l, r] の文字列)
    # s_len = random.randint(l, r)
    # s = "".join(random.choices(string.ascii_lowercase, k=s_len))

    # 4. 1次元配列 (例: 長さ [l, r] で、[b, u]の範囲の値の整数の配列)
    # a_len = random.randint(l, r)
    # a = [random.randint(b, u) for _ in range(a_len)]

    return input_str

def main():
    setup_directories()
    compile_cpp()
    
    exe_main = f"./{PROBLEM}_exe"
    exe_stupid = f"./{PROBLEM}_stupid_exe"
    
    print(f"Starting {NUM_TESTS} tests for problem {PROBLEM}...\n")
    
    for i in range(1, NUM_TESTS + 1):
        # 1. テストケース（入力）の生成
        input_data = generate_input()
        input_filename = os.path.join(DIR_INPUT, f"case_{i}.txt")
        with open(input_filename, "w", encoding="utf-8") as f:
            f.write(input_data)
            
        # 2. 本命解を実行
        output_filename = os.path.join(DIR_OUTPUT, f"case_{i}.txt")
        with open(input_filename, "r", encoding="utf-8") as fin, open(output_filename, "w", encoding="utf-8") as fout:
            subprocess.run([exe_main], stdin=fin, stdout=fout)
            
        # 3. 愚直解を実行
        output_stupid_filename = os.path.join(DIR_OUTPUT_STUPID, f"case_{i}.txt")
        with open(input_filename, "r", encoding="utf-8") as fin, open(output_stupid_filename, "w", encoding="utf-8") as fout:
            subprocess.run([exe_stupid], stdin=fin, stdout=fout)
            
        # 4. 結果の比較
        with open(output_filename, "r", encoding="utf-8") as f:
            out_main = f.read().strip()
        with open(output_stupid_filename, "r", encoding="utf-8") as f:
            out_stupid = f.read().strip()
            
        if out_main != out_stupid:
            print(f"[Mismatch] Test case {i} failed!")
            print(f"--- Input ---")
            print(input_data.strip())
            print(f"--- Your Output ({PROBLEM}.cpp) ---")
            print(out_main)
            print(f"--- Stupid Output ({PROBLEM}_stupid.cpp) ---")
            print(out_stupid)
            print("-" * 30)
            return

    print("All correct!")

if __name__ == "__main__":
    main()