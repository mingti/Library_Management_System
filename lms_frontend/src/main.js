import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

// element-plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import zhCn from 'element-plus/es/locale/lang/zh-cn'; //element-plus 中文语言包 修改分页总计显示为共 total 条
import 'element-plus/theme-chalk/dark/css-vars.css' // 暗黑模式

app.use(ElementPlus, {locale: zhCn});

// router
import router from './router'

app.use(router)

app.mount('#app')
