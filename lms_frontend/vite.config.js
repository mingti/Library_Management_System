import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'  // 关键：引入 Node.js 路径模块


// https://vite.dev/config/
export default defineConfig({
    plugins: [vue()],
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './src')  // 核心配置
        }
    }
})
