<script setup>
import {Icon} from "@iconify/vue";

import {Sunny, Moon} from '@element-plus/icons-vue'
import {ref} from "vue";


const RegisterDrawerShow = ref(false)
const LoginDrawerShow = ref(false)
const LoginButtonStyle = ref({
  bg: false,
  type: ''
})
const RegisterButtonStyle = ref({
  bg: false,
  type: ''
})

function ActiveButtonStyle(ButtonStyle) {
  ButtonStyle.value.bg = true
  ButtonStyle.value.type = 'primary'
}

function InactiveButtonStyle(ButtonStyle) {
  ButtonStyle.value.bg = false
  ButtonStyle.value.type = ''
}


function RegisterDrawerHandle() {
  LoginDrawerShow.value = false
  RegisterDrawerShow.value = true

  ActiveButtonStyle(RegisterButtonStyle)
  InactiveButtonStyle(LoginButtonStyle)

}

function LoginDrawerHandle() {
  RegisterDrawerShow.value = false
  LoginDrawerShow.value = true

  ActiveButtonStyle(LoginButtonStyle)
  InactiveButtonStyle(RegisterButtonStyle)
}


function ClearRegisterAndLoginButtonStyle() {
  RegisterDrawerShow.value = false
  LoginDrawerShow.value = false
  InactiveButtonStyle(RegisterButtonStyle)
  InactiveButtonStyle(LoginButtonStyle)
}


</script>

<template>
  <el-container>
    <el-header>
      <div class="el-header-left">
        <Icon icon="twemoji:books" width="32"/>
        <!--        <span style="font-family: 'Microsoft New Tai Lue'">书馆儿</span>-->
        <img src="@/assets/images/iconname/name.png" style="height: 30px" alt="">
      </div>
      <div class="el-header-right">
        <el-button text :bg="RegisterButtonStyle.bg" :type="RegisterButtonStyle.type" @click="RegisterDrawerHandle">
          注册
        </el-button>
        <el-button text :bg="LoginButtonStyle.bg" :type="LoginButtonStyle.type" @click="LoginDrawerHandle">
          登录
        </el-button>
      </div>
    </el-header>

    <el-drawer class="RightDrawer" v-model="RegisterDrawerShow" :before-close="ClearRegisterAndLoginButtonStyle"
               modal-class="DrawerModal" direction="ttb"
               :with-header="false">
      <span>注册</span>
    </el-drawer>
    <el-drawer class="RightDrawer" v-model="LoginDrawerShow" :before-close="ClearRegisterAndLoginButtonStyle"
               modal-class="DrawerModal" direction="ttb"
               :with-header="false">
      <span>登录</span>
    </el-drawer>
    <el-main>
      <div class="welcome-container">
        <h1 class="welcome-title">书卷多情似故人</h1>
        <p class="welcome-text">
          在字里行间漫游<br>
          开启您的沉浸式阅读体验
        </p>
      </div>
    </el-main>

  </el-container>

</template>

<style scoped>


.el-container {
  background-image: url('@/assets/images/backgrounds/bg4.jpg');
  background-size: cover;
  height: 100vh;
}

.el-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 2555; /*使el-drawer弹出时el-header还能显示,高于抽屉的默认 z-index (通常为 2000) */
}

.el-header-left {
  display: flex;
  align-items: center;
  column-gap: 12px;

}

.el-header-right {
  display: flex;
  align-items: center;
  column-gap: 12px;

}

/* 清除相邻el-button的默认左边距 */
.el-header-right .el-button + .el-button {
  margin-left: 0;
}


::v-deep(.RightDrawer) {
  opacity: 0.5;
  width: 40% !important;
  height: 100% !important;
  left: auto;
  right: 0;
}


/*把RegisterDrawerModal的半透明取消,这样同时还能点击额外区域推出elDrawer*/
:deep(.DrawerModal) {
  background-color: rgba(0, 0, 0, 0) !important; /* 透明度 0.3（更透明） */
}
.welcome-container {
  padding-left: 15%;
  padding-top: 20%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.welcome-title {
  color: #827575; /* 深咖啡色 */
  font-size: 4rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

.welcome-text {
  color: #7b7b7b;
  font-size: 1.5rem;
  opacity: 0.9;
  text-shadow: 0 2px 4px rgba(0,0,0,0.3);
}
</style>