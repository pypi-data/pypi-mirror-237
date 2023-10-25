import torch


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
            for current_gpu_index in range(num_gpu):
                # 获取当前GPU的名称
                info = {}
                info['name'] = torch.cuda.get_device_name(current_gpu_index)

                # 获取GPU显存的总量和已使用量
                info['totalMemory'] = torch.cuda.get_device_properties(current_gpu_index).total_memory / (
                        1024.0 ** 3)  # 显存总量(GB)
                info['usedMemory'] = torch.cuda.memory_allocated(current_gpu_index) / (1024.0 ** 3)  # 已使用显存(GB)
                info['freeMemory'] = info['totalMemory'] - info['usedMemory']  # 剩余显存(GB)
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

