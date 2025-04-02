from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)


class EnvWidget(QWidget):
    def __init__(self, env_data: dict, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.env_data = env_data
        self._init_ui()
        self._apply_styles()

    def _init_ui(self) -> None:
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setSpacing(16)
        self.layout.setContentsMargins(40, 40, 40, 40)

        self._create_header()
        self._create_section("Description", self._create_description())
        self._create_section("Action Space", self._create_action_space())
        self._create_section("Observation Space", self._create_observation_space())
        self._create_section("Rewards", self._create_rewards())
        self._create_section("Episode Information", self._create_episode_info())

    def _create_header(self) -> None:
        header = QFrame()
        header_layout = QVBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 0)

        display_name = QLabel(self.env_data.get("display_name", ""))
        display_name.setObjectName("env-name")

        env_id = QLabel(self.env_data["name"])
        env_id.setObjectName("env-id")

        category = QLabel(self.env_data["category"])
        category.setObjectName("env-category")

        header_layout.addWidget(display_name)
        header_layout.addWidget(env_id)
        header_layout.addWidget(category)
        self.layout.addWidget(header)

    def _create_section(self, title: str, content: QVBoxLayout) -> None:
        section = QFrame()
        section.setObjectName("env-section")
        layout = QVBoxLayout(section)

        title_label = QLabel(title)
        title_label.setObjectName("section-title")
        layout.addWidget(title_label)

        if isinstance(content, QWidget):
            layout.addWidget(content)
        else:
            layout.addLayout(content)

        self.layout.addWidget(section)

    def _create_description(self) -> QLabel:
        description = QLabel(self.env_data["description"])
        description.setObjectName("env-description")
        description.setWordWrap(True)
        return description

    def _create_action_space(self) -> QWidget:
        action_space = self.env_data["action_space"]
        container = QWidget()
        layout = QVBoxLayout(container)

        type_badge = QLabel(action_space["type"])
        type_badge.setObjectName("type-badge")
        layout.addWidget(type_badge)

        if "description" in action_space:
            desc = QLabel(action_space["description"])
            desc.setObjectName("space-description")
            layout.addWidget(desc)

        if action_space["type"] == "Discrete":
            grid = QGridLayout()
            grid.setHorizontalSpacing(15)
            grid.setVerticalSpacing(10)

            if "metadata" in action_space:
                for i, (key, value) in enumerate(action_space["metadata"].items()):
                    item_widget = QWidget()
                    item_widget.setObjectName("action-item")
                    item_layout = QHBoxLayout(item_widget)

                    number = QLabel(str(key))
                    number.setObjectName("action-number")
                    number.setAlignment(Qt.AlignCenter)

                    label = QLabel(value)
                    item_layout.addWidget(number)
                    item_layout.addWidget(label)
                    grid.addWidget(item_widget, i // 2, i % 2)

            layout.addLayout(grid)

        elif action_space["type"] == "Box":
            layout.addWidget(QLabel(f"Shape: {action_space['shape']}"))
            layout.addWidget(QLabel(f"Low: {action_space['low']}"))
            layout.addWidget(QLabel(f"High: {action_space['high']}"))

            if "metadata" in action_space:
                layout.addWidget(QLabel("Components:"))
                for key, value in action_space["metadata"].items():
                    layout.addWidget(QLabel(f"  {key}: {value}"))

        return container

    def _create_observation_space(self) -> QWidget:
        obs_space = self.env_data["observation_space"]
        container = QWidget()
        layout = QVBoxLayout(container)

        # Type badge
        type_badge = QLabel(obs_space["type"])
        type_badge.setObjectName("type-badge")
        layout.addWidget(type_badge)

        if "description" in obs_space:
            desc = QLabel(obs_space["description"])
            desc.setObjectName("space-description")
            layout.addWidget(desc)

        if obs_space["type"] == "Box":
            layout.addWidget(QLabel(f"Shape: {obs_space['shape']}"))
            layout.addWidget(QLabel(f"Low: {obs_space['low']}"))
            layout.addWidget(QLabel(f"High: {obs_space['high']}"))

            if "metadata" in obs_space:
                layout.addWidget(QLabel("Components:"))
                for key, value in obs_space["metadata"].items():
                    layout.addWidget(QLabel(f"  {key}: {value}"))

        return container

    def _create_rewards(self) -> QWidget:
        rewards = self.env_data["rewards"]
        container = QWidget()
        container.setObjectName("rewards-container")
        layout = QVBoxLayout(container)

        for reward_item, reward_value in rewards.items():
            self._add_reward_item(layout, reward_item, reward_value)

        return container

    def _add_reward_item(self, layout: QVBoxLayout, name: str, value: int) -> None:
        widget = QWidget()
        widget.setObjectName("reward-item")
        item_layout = QHBoxLayout(widget)
        item_layout.setContentsMargins(0, 0, 0, 0)

        name_label = QLabel(name.replace("_", " ").title())
        value_label = QLabel(f"{value}")
        value_label.setProperty("class", "positive" if value >= 0 else "negative")

        item_layout.addWidget(name_label)
        item_layout.addStretch()
        item_layout.addWidget(value_label)
        layout.addWidget(widget)

    def _create_episode_info(self) -> QWidget:
        container = QWidget()
        container.setObjectName("episode-container")
        grid = QGridLayout(container)

        start = QLabel(self.env_data["episode"]["start"])
        end = QLabel(self.env_data["episode"]["end"])

        grid.addWidget(self._create_episode_item("Start State", start), 0, 0)
        grid.addWidget(self._create_episode_item("End Conditions", end), 0, 1)

        return container

    def _create_episode_item(self, title: str, content: str) -> QWidget:
        widget = QFrame()
        widget.setObjectName("episode-item")
        layout = QVBoxLayout(widget)

        title_label = QLabel(title)
        title_label.setObjectName("episode-title")
        content.setWordWrap(True)

        layout.addWidget(title_label)
        layout.addWidget(content)
        return widget

    def _apply_styles(self) -> None:
        self.setStyleSheet(
            """
            QWidget {
                background: #ffffff;
                color: #374151;
                font-size: 15px;
            }
            
            /* Header Styles */
            #env-name {
                font-size: 34px;
                font-weight: 700;
                color: #111827;
                margin-bottom: 8px;
            }
            
            #env-id {
                color: #6b7280;
                font-size: 17px;
                margin-bottom: 12px;
            }
            
            #env-category {
                background: #f3f4f6;
                color: #374151;
                padding: 6px 14px;
                border-radius: 9999px;
                font-size: 14px;
                border: 1px solid #e5e7eb;
                margin-top: 16px;
            }
            
            /* Section Styles */
            #env-section {
                background: #ffffff;
                border: 1px solid #e5e7eb;
                border-radius: 12px;
                padding: 24px 32px;
                margin: 12px 0;
            }
            
            #section-title {
                font-size: 22px;
                font-weight: 700;
                color: #111827;
                margin-bottom: 18px;
            }
            
            /* Description Styles */
            #env-description {
                color: #6b7280;
                line-height: 1.6;
                margin-bottom: 18px;
                font-size: 16px;
            }
            
            /* Action Space Styles */
            #action-item {
                background: #ffffff;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 18px;
                margin: 8px;
            }
            
            #action-number {
                min-width: 38px;
                min-height: 38px;
                background: #f8fafc;
                color: #1e3a8a;
                border-radius: 6px;
                font-weight: 600;
                border: 1px solid #e2e8f0;
                font-size: 15px;
            }
            
            /* Type Badge */
            #type-badge {
                background: #f3f4f6;
                color: #374151;
                padding: 6px 16px;
                border-radius: 12px;
                font-weight: 600;
                font-size: 14px;
                margin-bottom: 12px;
            }
            
            /* Info Box Styles */
            #info-box {
                background: #f8fafc;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 20px;
                margin-top: 16px;
            }
            
            #info-row QLabel {
                color: #4b5563;
                font-size: 14px;
            }
            
            #values-grid QLabel {
                padding: 6px 12px;
                background: #ffffff;
                border-radius: 6px;
                margin: 2px;
            }
            
            /* Metadata Styles */
            #meta-container {
                margin-top: 16px;
                background: #ffffff;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 12px;
            }
            
            #meta-row {
                padding: 8px 12px;
                border-radius: 6px;
            }
            
            #meta-row:nth-child(odd) {
                background: #f9fafb;
            }
            
            /* Reward Styles */
            #reward-item {
                border-bottom: 1px solid #f1f5f9;
                padding: 14px 0;
            }
            
            .positive { 
                color: #059669;
                font-weight: 600;
            }
            
            .negative { 
                color: #dc2626;
                font-weight: 600;
            }
            
            /* Episode Styles */
            #episode-item {
                background: #ffffff;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                padding: 20px;
            }
            
            #episode-title {
                font-weight: 600;
                color: #111827;
                margin-bottom: 8px;
            }
        """
        )
