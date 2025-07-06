'use strict';
const AWS = require('aws-sdk');
const dynamodb = new AWS.DynamoDB.DocumentClient();
const TABLE_NAME = 'visitorLogs';

exports.handler = async (event) => {
  const headers = event.Records[0].cf.request.headers;
  const ip = headers['x-forwarded-for'][0].value;
  const user_agent = headers['user-agent'][0].value;
  const path = event.Records[0].cf.request.uri;
  const params = {
    TableName: TABLE_NAME,
    Item: {
      id: `${Date.now()}-${Math.floor(Math.random()*1000)}`,
      ip,
      user_agent,
      path,
      timestamp: new Date().toISOString()
    }
  };
  try {
    await dynamodb.put(params).promise();
    console.log("Visitor log stored.");
  } catch (err) {
    console.error("Error storing visitor log:", err);
  }
  return event.Records[0].cf.request;
};
