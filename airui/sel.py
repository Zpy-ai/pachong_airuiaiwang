from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 创建 EdgeOptions 对象，用于配置浏览器选项
edge_options = Options()
# 添加参数忽略证书错误
edge_options.add_argument('--ignore-certificate-errors')
# 添加参数禁用扩展
edge_options.add_argument('--disable-extensions')
# 添加参数禁用沙盒模式
edge_options.add_argument('--no-sandbox')
# 添加参数禁用 GPU 加速
edge_options.add_argument('--disable-gpu')

# 创建 Edge 浏览器驱动实例
driver = webdriver.Edge(options=edge_options)

url = 'https://report.iresearch.cn/'

# 打开指定 URL 的网页
driver.get(url)

try:
    # 用于保存找到的元素信息
    found_elements_info = []
    found_links = []
    
    wait = WebDriverWait(driver, 10)
    # 1. 点击"加载更多"按钮10次
    load_count = 0
    while load_count < 10:
        try:
            # 定位"加载更多"按钮
            load_more_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button#loadbtn')  # 根据实际页面调整选择器
                )
            )
            
            # 点击按钮
            load_more_btn.click()
            load_count += 1
            print(f"已点击加载更多 {load_count}/10 次")
            
            # 等待新内容加载（根据页面加载速度调整）
            time.sleep(2)
            
        except Exception as e:
            print(f"点击加载更多失败: {e}")
            break
    
    # 2. 等待所有内容加载完成
    print("等待内容加载完成...")
    time.sleep(3)  # 额外等待确保所有内容加载完成
    
    # 3. 遍历所有找到的元素（包括初始加载和点击加载的）
    elements = driver.find_elements(By.CSS_SELECTOR, 'li[id^="freport."]')
    print(f"共找到 {len(elements)} 个元素")
    
    if elements:
        for elem in elements:
            element_text = elem.text
            
            # 提取链接（处理可能的异常）
            try:
                a_element = elem.find_element(By.CSS_SELECTOR, 'a')
                element_link = a_element.get_attribute('href')
                found_links.append(element_link)
            except:
                element_link = "未找到链接"
            
            # 保存信息
            found_elements_info.append(f"文本内容: {element_text}, 链接: {element_link}")
            print("找到元素：", element_text[:30] + "...")  # 只打印前30个字符避免刷屏
        
        # 4. 将找到的元素信息保存到文件
        with open('found_elements.txt', 'w', encoding='utf-8') as f:
            for info in found_elements_info:
                f.write(info + '\n')
        print("已将找到的元素信息保存到 found_elements.txt")
        
        # 5. 将找到的链接信息保存到文件
        with open('found_links.txt', 'w', encoding='utf-8') as f:
            for link in found_links:
                f.write(link + '\n')
        print("已将找到的链接信息保存到 found_links.txt")
    else:
        print("未找到符合条件的元素。")

except Exception as e:
    print("定位元素失败：", e)
    # 获取页面源代码，用于调试
    page_source = driver.page_source
    with open('page_source.html', 'w', encoding='utf-8') as f:
        f.write(page_source)
    print("已将页面源代码保存到 page_source.html，请查看分析")
finally:
    # 确保浏览器最终会被关闭
    time.sleep(2)  # 可根据需要调整等待时间，方便观察页面
    driver.quit()