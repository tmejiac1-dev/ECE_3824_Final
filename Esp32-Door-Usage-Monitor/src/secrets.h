#ifndef SECRETS_H
#define SECRETS_H
// Wifi configuration
constexpr const char* ssidList[] = {
  "ssovo(2.4)",
  "ovo",
  "ssovo"
};

constexpr const char* passwordList[] = {
  "LanZhaoXiang0607",
  "20030607",
  "20030607"
};

constexpr int wifiCount = sizeof(ssidList) / sizeof(ssidList[0]);

constexpr const char* serverUrl = "https://project-mqrua.vercel.app/api/data";// Sserver URL

constexpr const char* apiKey = "LanZhaoXiang123"; // API key for backend authentication


#endif 