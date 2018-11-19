(* ::Package:: *)

BeginPackage["PredictionModelNUSWorkshop`", {"WebServicesServer`","MSP`", "XMLSchema`"}]

PredictionModel::usage = "Predicts step on voltage"



Begin["`Private`"]
PredictionModel[DesiredTemparature_String,UserID_String,TestingFlag_String] :=
	Module[{},
DatabasePath=MSPPageDirectory[];	

SetDirectory[MSPPageDirectory[]];
datafile=FileNameJoin[{Directory[],"obs_data_w.xlsx"}];

datasetnb = Import[datafile][[1]];
datasetnb =Drop[ datasetnb,1];
datalengthnb = Length[datasetnb];

Voltage = {};
CurrentDensity= {};
Temparature = {};
Uncertanity= {};
c1 = 0;
While[(c1 += 1) <datalengthnb ,
  {
    
    Voltage = Append[Voltage, datasetnb[[c1]][[2]]];
    Temparature = Append[Temparature, datasetnb[[c1]][[3]]];
    Uncertanity = Append[Uncertanity, datasetnb[[c1]][[4]]];
    CurrentDensity = Append[CurrentDensity, datasetnb[[c1]][[5]]];
    };
  ];

inputset= Transpose[{Temparature,CurrentDensity}];
completeset= {};
For[i=1,i<datalengthnb,i++,completeset = Append[completeset,inputset[[i]] -> Voltage[[i]]]];
CompletesetRandomized=completeset[[PermutationList@RandomPermutation@Length[completeset]]];
TrainTestRatio = 0.8;
{TrainingSet,TestSet}=TakeDrop[CompletesetRandomized,Round[Length[CompletesetRandomized]*TrainTestRatio]];

RandomForestPrediction= Predict[TrainingSet,Method->"RandomForest"];

DesiredConditions = {ToExpression[DesiredTemparature],0.1};	
PredictedVonbyRFMethod = RandomForestPrediction[DesiredConditions];


OutputValueraw = ExportString[<|"input"-><|"User_Information"-><|"UserID"->UserID,"Testing"->TestingFlag,"OutputFormat"-> "OutputForm"|>,"Parameters"-><|"status"-> "true","keys"-> {"DesiredTemparature"},"values"-> {DesiredTemparature}|>|>,
  "Von_Predicted"->  <|"unit" -> "volts", "description" -> "Von predicted using Random Forest method in Mathematica prediction model", "abbrevation" -> "V","value" -> PredictedVonbyRFMethod|>|>, "RawJSON","Compact" -> True]
   

    ]
ServiceReturn[PredictionModel] = _SchemaExpr

End[]
EndPackage[]

