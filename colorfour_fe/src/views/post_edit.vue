<template>
  <div>
    <div id="header"></div>
    <main class="main-content container">
      <div class="left-sidebar">
        <div class="icon-search">
          <img src="@/assets/img/search_icon.png" alt="Search Icon" />
          <input type="text" placeholder="search" />
        </div>

        <div class="icon-link">
          <router-link to="social_index">
            <img src="@/assets/img/social_home_icon.png" alt="Home Icon" />
            <span>社群平台首頁</span>
          </router-link>
        </div>

        <div class="icon-link">
          <router-link to="social_collect">
            <img src="@/assets/img/like_icon.png" alt="Saved Posts Icon" />
            <span>收藏貼文</span>
          </router-link>
        </div>

        <div class="icon-link">
          <router-link to="social_follow_list">
            <img src="@/assets/img/followers_icon.png" alt="Overview Icon" />
            <span>追蹤總覽</span>
          </router-link>
        </div>
      </div>

      <div id="edit-post-container" class="content">
        <div class="edit-post mb-5">
          <h2 class="edit-post-title">修改貼文</h2>
          <form @submit.prevent="updatePost">
            <div class="form-group mb-3">
              <label for="postDescription">貼文描述</label>
              <textarea
                v-model="post.description"
                id="postDescription"
                class="form-control"
                rows="4"
                placeholder="輸入貼文描述..."
              ></textarea>
            </div>

            <div class="form-group mb-3">
              <label for="postHashtags">標籤</label>
              <input
                type="text"
                v-model="post.hashtags"
                id="postHashtags"
                class="form-control"
                placeholder="#標籤"
              />
            </div>

            <div class="form-group mb-3">
              <label for="postLocation">地點</label>
              <input
                type="text"
                v-model="post.location"
                id="postLocation"
                class="form-control"
                placeholder="輸入地點"
              />
            </div>

            <div class="form-group mb-3">
              <label for="postTime">時間</label>
              <input
                type="datetime-local"
                v-model="post.time"
                id="postTime"
                class="form-control"
              />
            </div>

            <div class="form-group mb-3">
              <label for="postImage">貼文圖片</label>
              <input type="file" @change="onImageChange" id="postImage" class="form-control-file" />
            </div>

            <div class="form-group">
              <button type="submit" class="btn btn-primary">保存變更</button>
              <router-link to="social_index" class="btn btn-secondary ms-3">取消</router-link>
            </div>
          </form>
        </div>
      </div>
    </main>
    <div class="zone"></div>
    <div id="footer"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      post: {
        id: "",
        username: "",
        description: "",
        hashtags: "",
        location: "",
        time: "",
        image: "",
      },
    };
  },
  mounted() {
    this.fetchPost();
  },
  methods: {
    fetchPost() {
      const postId = parseInt(this.$route.params.postId);
      console.log('Fetching post with ID:', postId);

      const posts = [
        {
          id: 1,
          username: "嗡嗡嗡",
          description: "今日OOTD，鄰家妹妹vs帥氣姐姐，更喜歡哪個~~😍",
          hashtags: "#OOTD #帥氣 #甜美",
          location: "中原大學",
          time: "2024-04-18T10:00",
          image: require('@/assets/img/post_01.jpg'),
        },
        {
          id: 2,
          username: "哇哈哈",
          description: "今天天氣真好，出門散步拍了些美照。",
          hashtags: "#散步 #美照 #好心情",
          location: "台北市",
          time: "2024-04-17T10:00",
          image: "https://picsum.photos/300/200?random=1",
        },
        {
          id: 3,
          username: "小明",
          description: "剛完成了一幅新畫作，分享給大家看看。",
          hashtags: "#畫作 #藝術 #分享",
          location: "高雄市",
          time: "2024-04-16",
          image: "https://picsum.photos/300/200?random=2",
        },
      ];

      const post = posts.find(p => p.id === postId);
      if (post) {
        console.log('Post found:', post);
        this.post = { ...post };
      } else {
        console.error('Post not found');
      }
    },
    onImageChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.post.image = URL.createObjectURL(file);
      }
    },
    updatePost() {
      // 更新貼文的邏輯
      console.log('更新貼文:', this.post);
      this.$router.push({ name: 'social_index' }); // 返回社群平台首頁
    },
  },
};

</script>


<style scoped>
.main-content {
  width: 90%;
  position: relative;
  display: flex;
  flex-direction: column;
}

.edit-post {
  width: 100%;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  max-width: 600px;
  background-color: #fff;
  color: rgb(8, 8, 8);
  text-align: left;
}

.edit-post-title {
  text-align: center;
  margin-bottom: 20px;
  font-size: 1.5em;
}

.form-group label {
  font-weight: bold;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border-radius: 5px;
  border: 1px solid #ddd;
}

.form-group textarea {
  resize: vertical;
}

.form-group .btn {
  background-color: #f0a9a9;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  color: white;
}

.form-group .btn:hover {
  background-color: #e09393;
}

.form-group .btn-secondary {
  background-color: #cccccc;
}

.form-group .btn-secondary:hover {
  background-color: #bbbbbb;
}

@media screen and (max-width: 800px) {
  .slider {
    margin: 20px auto;
  }

  .slide img {
    border-radius: 20px;
  }

  .post {
    padding: 10px;
    margin: 10px 0;
    border-radius: 20px;
  }

  .post-actions button {
    padding: 5px 10px;
  }
}


/* 确保左侧边栏在大屏幕时显示 */
.left-sidebar {
  width: 200px;
  background-color: #f0f0f0;
  padding: 20px;
  position: fixed;
  top: 70px;
  left: 0;
  height: calc(100% - 120px);
  overflow-y: auto;
  z-index: 10;
  transition: all 0.3s ease;
}


.left-sidebar .icon-search,
.left-sidebar .icon-link {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.left-sidebar .icon-search img,
.left-sidebar .icon-link img {
  margin-right: 10px;
  width: 30px;
  height: 30px;
  transition: all 0.3s ease;
}

.left-sidebar .icon-search input {
  flex: 1;
}

.left-sidebar .icon-link a {
  text-decoration: none;
  color: var(--primary-text-color);
  font-weight: 600;
  transition: all 0.3s ease;
  
}

/* 小屏幕样式 */
@media (max-width: 768px) {
  .left-sidebar {
    width: 100%;
    position: fixed;
    top: 60px;
    left: 0;
    height: 60px;
    display: flex;
    justify-content: space-around;
    padding: 15px;
    background-color: var(--header-footer-bg-color);
  }

  .main-content {
    margin-top: 90px;
  }

  .left-sidebar .icon-search {
    display: none; /* 隐藏搜索栏位 */
  }

  .left-sidebar .icon-link {
    flex-direction: column;
    align-items: center;
    margin-bottom: 0;
  }

  .left-sidebar .icon-link span {
    display: none; /* 隐藏文字 */
  }

  .left-sidebar .icon-link img {
    margin-right: 0;
    width: 40px;
    height: 40px;
  }
}
</style>
