document.addEventListener('DOMContentLoaded', function() {
  // 获取DOM元素
  const floatButton = document.getElementById('ai-chat-float-button');
  const chatDialog = document.getElementById('ai-chat-dialog');
  const closeBtn = chatDialog.querySelector('.close-btn');
  const sendBtn = document.getElementById('send-btn');
  const questionInput = document.getElementById('question-input');
  const chatMessages = document.getElementById('chat-messages');
  const userLoggedIn = document.querySelector('meta[name="user-logged-in"]').content === 'true';

  // 未登录状态下隐藏悬浮球
  if (!userLoggedIn) {
    floatButton.style.display = 'none';
    return;
  }

  // 悬浮球点击事件 - 切换对话框显示
  floatButton.addEventListener('click', function() {
    chatDialog.classList.toggle('active');
  });

  // 关闭按钮点击事件
  closeBtn.addEventListener('click', function() {
    chatDialog.classList.remove('active');
  });

  // 发送按钮点击事件
  sendBtn.addEventListener('click', sendMessage);

  // 输入框回车事件
  questionInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      sendMessage();
    }
  });

  // 发送消息函数
  function sendMessage() {
    const question = questionInput.value.trim();
    if (!question) return;

    // 添加用户消息到聊天窗口
    addMessageToChat(question, 'user');
    questionInput.value = '';

    // 显示加载状态
    addMessageToChat('正在思考...', 'ai', true);

    // 发送请求到API
    fetch('/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question: question })
    })
    .then(response => {
      if (!response.ok) throw new Error('请求失败');
      return response.json();
    })
    .then(data => {
      // 移除加载状态并添加AI回复
      removeLoadingMessage();
      addMessageToChat(data.answer, 'ai');
    })
    .catch(error => {
      // 移除加载状态并显示错误消息
      removeLoadingMessage();
      addMessageToChat('抱歉，无法获取回答: ' + error.message, 'ai');
    });
  }

  // 添加消息到聊天窗口
  function addMessageToChat(text, sender, isLoading = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${sender}-message`;
    if (isLoading) {
      messageDiv.classList.add('loading');
      messageDiv.id = 'loading-message';
    }
    messageDiv.textContent = text;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // 移除加载消息
  function removeLoadingMessage() {
    const loadingMessage = document.getElementById('loading-message');
    if (loadingMessage) {
      chatMessages.removeChild(loadingMessage);
    }
  }
});