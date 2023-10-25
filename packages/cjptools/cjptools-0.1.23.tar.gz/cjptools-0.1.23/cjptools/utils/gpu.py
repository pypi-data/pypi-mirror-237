import torch
import subprocess

class GpuMemory(object):
    def __init__(self):
        pass

    def getInfo(self):
        res = {}
        res['torchVersion'] = torch.__version__
        cuda_available = torch.cuda.is_available()
        res['cudaAvailable'] = cuda_available
        if cuda_available:
            # 获取GPU设备数量
            num_gpu = torch.cuda.device_count()
            res['gpuNum'] = num_gpu
            res['gpuInfo'] = []

            command = 'nvidia-smi --query-gpu=memory.total --format=csv'
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            output = result.stdout.strip().split('\n')[1:]  # 删除标题行
            total_memory = [float(line.split(',')[0].strip().split(' ')[0].strip()) for line in output]
            command = 'nvidia-smi --query-gpu=memory.used --format=csv'
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            output = result.stdout.strip().split('\n')[1:]  # 删除标题行
            used_memory = [float(line.split(',')[0].strip().split(' ')[0].strip()) for line in output]
            command = 'nvidia-smi --query-gpu=memory.free --format=csv'
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            output = result.stdout.strip().split('\n')[1:]  # 删除标题行
            free_memory = [float(line.split(',')[0].strip().split(' ')[0].strip()) for line in output]

            for current_gpu_index in range(num_gpu):
                # 获取当前GPU的名称
                info = {}
                info['name'] = torch.cuda.get_device_name(current_gpu_index)

                # 获取GPU显存的总量和已使用量
                info['totalMemory'] = total_memory[current_gpu_index] / 1024.0  # 显存总量(GB)
                info['usedMemory'] = used_memory[current_gpu_index] / 1024.0  # 已使用显存(GB)
                info['freeMemory'] = free_memory[current_gpu_index] / 1024.0  # 剩余显存(GB)
                res['gpuInfo'].append(info)
        return res;

    def __str__(self):
        res = self.getInfo()
        ss = ''
        ss += f"PyTorch版本：{res['torchVersion']}\n"
        if res['cudaAvailable']:
            ss += f"CUDA可用，共有 {res['gpuNum']} 个GPU设备可用。\n"
            for current_gpu_index, info in enumerate(res['gpuInfo']):
                ss += f"第{current_gpu_index}块显卡信息如下：\n"
                ss += f"\tGPU设备名称：{info['name']}\n"
                ss += f"\tGPU显存总量：{info['totalMemory']:.2f} GB\n"
                ss += f"\t已使用的GPU显存：{info['usedMemory']:.2f} GB\n"
                ss += f"\t剩余GPU显存：{info['freeMemory']:.2f} GB\n"
        else:
            ss = "CUDA不可用。\n"
        return ss

    def gpuIdWithMaxFree(self):
        res = self.getInfo()
        ind = -1;
        freeMemory = 0
        name = ''
        for current_gpu_index, info in enumerate(res['gpuInfo']):
            if info['freeMemory'] > freeMemory:
                freeMemory = info['freeMemory']
                ind = current_gpu_index
                name = info['name']
        return ind, freeMemory, name

if __name__ == "__main__":
    mem=GpuMemory()
    print(mem)