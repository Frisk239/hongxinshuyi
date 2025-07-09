// 初始化粒子效果
document.addEventListener('DOMContentLoaded', function() {
    // 粒子效果配置
    particlesJS('particles-js', {
        particles: {
            number: {
                value: 80,
                density: {
                    enable: true,
                    value_area: 800
                }
            },
            color: {
                value: "#c12c2c"
            },
            shape: {
                type: "circle",
                stroke: {
                    width: 0,
                    color: "#000000"
                }
            },
            opacity: {
                value: 0.5,
                random: true,
                anim: {
                    enable: true,
                    speed: 1,
                    opacity_min: 0.1,
                    sync: false
                }
            },
            size: {
                value: 3,
                random: true,
                anim: {
                    enable: true,
                    speed: 2,
                    size_min: 0.1,
                    sync: false
                }
            },
            line_linked: {
                enable: true,
                distance: 150,
                color: "#c12c2c",
                opacity: 0.4,
                width: 1
            },
            move: {
                enable: true,
                speed: 2,
                direction: "none",
                random: true,
                straight: false,
                out_mode: "out",
                bounce: false,
                attract: {
                    enable: false,
                    rotateX: 600,
                    rotateY: 1200
                }
            }
        },
        interactivity: {
            detect_on: "canvas",
            events: {
                onhover: {
                    enable: true,
                    mode: "grab"
                },
                onclick: {
                    enable: true,
                    mode: "push"
                },
                resize: true
            },
            modes: {
                grab: {
                    distance: 140,
                    line_linked: {
                        opacity: 1
                    }
                },
                push: {
                    particles_nb: 4
                }
            }
        },
        retina_detect: true
    });

    // AI聊天弹窗控制
    const chatModal = document.getElementById('ai-chat-modal');
    const closeBtn = document.querySelector('.close-btn');
    const searchBtn = document.getElementById('search-btn');
    const sendBtn = document.getElementById('send-btn');
    const chatContainer = document.getElementById('chat-container');
    const userInput = document.getElementById('user-input');

    // 搜索按钮点击事件
    searchBtn?.addEventListener('click', function() {
        const searchText = document.getElementById('search-input').value;
        if (searchText.trim()) {
            openChatModal();
            addMessage('user', searchText);
            getAIResponse(searchText);
        }
    });

    // 打开聊天弹窗
    function openChatModal() {
        chatModal.style.display = 'flex';
    }

    // 关闭聊天弹窗
    closeBtn?.addEventListener('click', function() {
        chatModal.style.display = 'none';
    });

    // 发送消息
    sendBtn?.addEventListener('click', function() {
        const message = userInput.value.trim();
        if (message) {
            addMessage('user', message);
            userInput.value = '';
            getAIResponse(message);
        }
    });

    // 添加消息到聊天窗口
    function addMessage(role, content) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}`;
        messageDiv.textContent = content;
        chatContainer.appendChild(messageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    // 获取AI回复
    function getAIResponse(query) {
        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: query
            })
        })
        .then(response => response.json())
        .then(data => {
            addMessage('assistant', data.response);
        })
        .catch(error => {
            addMessage('assistant', '抱歉，获取回答时出错，请稍后再试。');
            console.error('Error:', error);
        });
    }

    // 用户头像点击事件
    document.getElementById('avatar-img')?.addEventListener('click', function() {
        // 检查用户是否登录
        fetch('/api/check-login')
            .then(response => response.json())
            .then(data => {
                if (data.logged_in) {
                    window.location.href = '/user-center';
                } else {
                    window.location.href = '/login';
                }
            });
    });
});
