#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "ditt-ssid";
const char* password = "ditt-passord";

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }

    Serial.println("Connected to WiFi");
}

void loop() {
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;

        // Anta at vi har data fra blodtrykksmåleren
        int systolic = 120;
        int diastolic = 80;
        int pulse = 75;

        // Endre med din Django server-URL
        http.begin("http://django-server.com/api/bloodpressure/");
        http.addHeader("Content-Type", "application/json");

        // Formatering av data til JSON
        String httpRequestData = "{\"systolic\":\"" + String(systolic) + "\", \"diastolic\":\"" + String(diastolic) + "\", \"pulse\":\"" + String(pulse) + "\"}";
        
        int httpResponseCode = http.POST(httpRequestData);

        if (httpResponseCode > 0) {
            Serial.print("HTTP Response code: ");
            Serial.println(httpResponseCode);
            String payload = http.getString();
            Serial.println(payload);
        }
        else {
            Serial.print("Error code: ");
            Serial.println(httpResponseCode);
        }
        http.end();
    }
    else {
        Serial.println("WiFi Disconnected");
    }
    delay(10000);  // Sender ny data hvert 10. sekund
}
