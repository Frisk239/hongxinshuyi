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

    // 搜索按钮点击事件 - 仅保留视觉元素
    const searchBtn = document.getElementById('search-btn');
    searchBtn?.addEventListener('click', function(e) {
        e.preventDefault();
        alert('搜索功能已禁用');
    });

    // 阻止搜索框回车键自动提交
    document.getElementById('search-input')?.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            alert('搜索功能已禁用');
        }
    });

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

    // 修改密码弹窗逻辑
    document.getElementById('change-password-btn')?.addEventListener('click', function(e) {
        e.preventDefault();
        document.getElementById('change-password-modal').style.display = 'flex';
    });

    document.getElementById('confirm-change-password')?.addEventListener('click', function() {
        const oldPassword = document.getElementById('old-password').value;
        const newPassword = document.getElementById('new-password').value;

        fetch('/api/change-password', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                old_password: oldPassword,
                new_password: newPassword
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('密码修改成功');
                document.getElementById('change-password-modal').style.display = 'none';
            } else {
                alert(data.error || '密码修改失败');
            }
        });
    });

    document.getElementById('cancel-change-password')?.addEventListener('click', function() {
        document.getElementById('change-password-modal').style.display = 'none';
    });
});
