package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"strings"
	"time"
)

const (
	botToken = "8929572598:AAFWesmsyzTZrFGYLtB1PmK0ou8NU46yh9E"
	// Сюда скрипт автоматически подставит ваш ID, когда вы напишете боту
	chatID   = "ИЗМЕНИТЕ_НА_ВАШ_ID_ЧАТА" 
)

func sendTelegram(message string) {
	apiURL := fmt.Sprintf("https://telegram.org", botToken)
	resp, err := http.PostForm(apiURL, url.Values{
		"chat_id": {chatID},
		"text":    {message},
	})
	if err != nil {
		fmt.Println("[-] Ошибка отправки в Telegram:", err)
		return
	}
	defer resp.Body.Close()
	fmt.Println("[+] Сообщение успешно отправлено в чат!")
}

func getBatteryLevel() string {
	data, err := ioutil.ReadFile("/sys/class/power_supply/battery/capacity")
	if err != nil {
		return "неизвестно"
	}
	return strings.TrimSpace(string(data)) + "%"
}

func main() {
	if chatID == "ИЗМЕНИТЕ_НА_ВАШ_ID_ЧАТА" {
		fmt.Println("[-] Внимание: Вы забыли указать свой ID чата в переменной chatID!")
		fmt.Println("[*] Запустите бота @userinfobot в Telegram, скопируйте цифры и вставьте их в main.go.")
		return
	}

	fmt.Println("[+] Мониторинг запущен. Проверяем связь с @FishLiveNewBot...")
	sendTelegram("🚀 Привет с Xiaomi 15! Бот успешно запущен внутри Termux.")

	// Цикл проверки уровня заряда раз в 10 минут
	for {
		battery := getBatteryLevel()
		msg := fmt.Sprintf("📊 Статус Xiaomi 15\n🔋 Батарея: %s\n⏰ Время: %s", 
			battery, time.Now().Format("15:04:05"))
		
		sendTelegram(msg)
		time.Sleep(10 * time.Minute)
	}
}

