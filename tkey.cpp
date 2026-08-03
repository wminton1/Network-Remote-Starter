#include <WiFi.h>
#include <HTTPClient.h>

// Network Credentials
const char* ssid     = "ATTcqpZVvS";
const char* password = "4pu4daex+xnu";

// Your Raspberry Pi's fixed local IP address and Flask port
const char* serverUrl = "http://192.168.1";

const int BUTTON_PIN = 4; // GPIO pin connected to your button


void setup() {
    Serial.begin(115200);
    pinMode(BUTTON_PIN, INPUT_PULLUP); // Keeps pin HIGH until button connects it to GND

  // Connect to Wi-Fi network
WiFi.begin(ssid, password);
while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
}
Serial.println("\nWiFi Connected!");
}

void loop() {
  // If button is pressed, the pin reads LOW
if (digitalRead(BUTTON_PIN) == LOW) {
    Serial.println("Button pressed! Signaling Batman Command Center...");

    if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);

      // Send a blank POST request to trigger the Pi
    int httpResponseCode = http.POST(""); 

    if (httpResponseCode > 0) {
        Serial.printf("Response from Pi: %d\n", httpResponseCode);
    } else {
        Serial.printf("Error signaling Pi: %s\n", http.errorToString(httpResponseCode).c_str());
    }
    
    http.end();
    }
    
    // Debounce/Cool-down delay so a single physical click doesn't trigger 100 requests
    delay(2000); 
}
}
